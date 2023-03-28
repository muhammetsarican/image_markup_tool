import cv2, os, json, keyboard
from threading import Thread
import pyautogui

with open("filePath.json", "r", encoding="utf-8") as file:
    paths=json.load(file)
    
paths=paths["win_path"]

class ImageSection:
    isUiFirstLoad = True
    frameLocationsList = []
    
    frame = cv2.imread(paths["image_path"])
    # frame=cv2.resize(frame, None, fx=0, fy=0)

    signedFrame=frame.copy()
    notSignedFrame = frame.copy()
    # frame=cv2.resize(frame,(600,600))
    # print(frame.shape)
    frame_width = 50
    frame_height = 60
    width = frame.shape[1]
    height = frame.shape[0]
    
    def getParts(self):
        return int(self.frame.shape[1]/pyautogui.size()[0]), int(self.frame.shape[0]/pyautogui.size()[1])# It sends width first, height second
    
    def fileCounter(self):
        fileCounter=0
        for path in os.listdir(paths["image_save_path"]):
            for _ in os.listdir(paths["image_save_path"]+path):
                fileCounter+=1
        return fileCounter
    
    def radiobutton_event(self, ui):
        print("Height radiobutton toggled, current value:", ui.heightVar.get())
        print("Width radiobutton toggled, current value:", ui.widthVar.get())
        
    upsideORdownside=True
    width_start=0
    height_start=0  
    
    def getBaseImage(self, ui=None):
        if ui is not None:
            self.width_start=ui.widthVar.get()*pyautogui.size()[0]
            self.height_start=ui.heightVar.get()*pyautogui.size()[1]
            print(f"Ui: {self.width_start, self.height_start}")
        
        width_end=self.width_start+pyautogui.size()[0]
        height_end=self.height_start+pyautogui.size()[1]

        frame = self.signedFrame[self.height_start:height_end, self.width_start:width_end, :]
        return frame, self.height_start, height_end, self.width_start, width_end

    def __init__(self) -> None:
        pass
    def start(self):
        self.takeFrameThread = Thread(target=self.takeFrame, args=())
        self.takeFrameThread.daemon=True
        self.takeFrameThread.start()
        
    def findMarkedImages(self):
        with open("frameLocations.json", "r", encoding="utf-8") as file:
            self.frameLocationsList = json.load(file)

        for item in self.frameLocationsList:
            if item["source_image_path"] == paths["image_path"]:
                if os.path.exists(item["resized_image_path"]):
                    cv2.putText(self.signedFrame, item["resized_image_path"].split("/")[-2], (item["start_x"]+5, item["start_y"]+75), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
                    cv2.rectangle(self.signedFrame, (item["start_x"], item["start_y"]),
                                  (item["end_x"], item["end_y"]), (0, 100, 255), 2)

    def saveResizedImage(self, choice, root):
        _, height_start, height_end, width_start, width_end=self.getBaseImage()
        # print(data_path+choice.get())
        # for path in os.listdir(data_path+choice.get()):
        #     print(path)
        # print(self.bbox[1], self.bbox[1]+frame_height, self.bbox[0], self.bbox[0]+frame_width)

        # with open('frameLocations.json', "r", encoding='utf-8') as file:
        #     try:
        #         self.frameLocationsList=json.load(file)
        #     except Exception as E:
        #         print(E)
        # print(self.frameLocationsList)
        frameLocation = {
            "source_image_path": paths["image_path"],
            "resized_image_path": f"{paths['image_save_path']+choice.get()}/{self.fileCounter()}.jpg",
            "start_x": self.bbox[0]+width_start,
            "start_y": self.bbox[1]+height_start,
            "end_x": self.bbox[0]+self.bbox[2]+width_start,
            "end_y": self.bbox[1]+self.bbox[3]+height_start
        }
        self.frameLocationsList.append(frameLocation)
        with open('frameLocations.json', 'w', encoding='UTF-8') as file:
            json.dump(self.frameLocationsList, file,
                      ensure_ascii=False, indent=4)
            # file.write(f"source_image_path={path},resized_image_path={data_path+choice.get()}/{self.fileCounter()}.jpg,start_x={self.bbox[0]},start_y={self.bbox[1]},end_x={self.bbox[0]+frame_width},end_y={self.bbox[1]+frame_height}\n")

        cv2.rectangle(self.frame, (self.bbox[0], self.bbox[1]), (
            self.bbox[0]+self.bbox[2], self.bbox[1]+self.bbox[3]), (0, 255, 0), 1)
        cv2.putText(self.frame, choice.get(
        ), (self.bbox[0]+5, self.bbox[1]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        cv2.imwrite(f"{paths['image_save_path']+choice.get()}/{self.fileCounter()}.jpg", self.image)
        # cv2.destroyAllWindows()
        # takeFrameThread.kill()
        self.start()
    # print(f"{int(self.bbox[1])}:{int(self.bbox[1]+self.bbox[3])},{int(self.bbox[0])}:{int(self.bbox[0]+self.bbox[2])}")

    def takeFrame(self):
        frame, height_start, height_end, width_start, width_end=self.getBaseImage()
        self.findMarkedImages()                 
        self.bbox = cv2.selectROI(frame)
        cv2.destroyAllWindows()
        # cv2.waitKey(0)
        # self.takeFrameThread.cancel()
        # cv2.destroyAllWindows()
        if(self.bbox[2]<50 or self.bbox[3]<60):
            self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.frame_height+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+self.frame_width+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
        else:
            self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.bbox[3]+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+self.bbox[2]+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
            self.image=cv2.resize(self.image, (self.frame_width, self.frame_height))
        # cv2.imshow("notSignedFrame", self.image)
        # cv2.waitKey(0)
        
    def passMarking(self):
        # cv2.destroyWindow("notSignedFrame")
        self.start()
        
    def closeUI(self):
        try:
            if self.bbox:
                pass
        except:
            keyboard.press_and_release("c")

        r_frame=cv2.resize(self.signedFrame, (pyautogui.size()[0]-100, pyautogui.size()[1]-100))
        cv2.imshow("frame", r_frame)
        cv2.waitKey(0)