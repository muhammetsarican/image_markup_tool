import cv2, os, json, keyboard
from threading import Thread

with open("filePath.json", "r", encoding="utf-8") as file:
    paths=json.load(file)

paths=paths["win_path"]
class ImageSection:
    isUiFirstLoad = True
    frameLocationsList = []
    
    frame = cv2.imread(paths["image_path"])

    signedFrame=frame.copy()
    notSignedFrame = frame.copy()
    # frame=cv2.resize(frame,(600,600))
    # print(frame.shape)
    frame_width = 50
    frame_height = 60
    width = frame.shape[1]
    height = frame.shape[0]
    
    upsideORdownside=True
    def getBaseImage(self):
        if self.upsideORdownside:
            height_start=int(0)
            height_end=int(self.height/2)
        else:
            height_start=int(self.height/2)
            height_end=int(self.height)
            
        frame = self.signedFrame[height_start:height_end, 0:self.width, :]
        return frame, height_start, height_end    

    def __init__(self) -> None:
        pass
    def start(self):
        print("start")
        self.takeFrameThread = Thread(target=self.takeFrame, args=())
        self.takeFrameThread.daemon=True
        self.takeFrameThread.start()
        
    def findMarkedImages(self):
        with open("frameLocations.json", "r", encoding="utf-8") as file:
            self.frameLocationsList = json.load(file)

        for item in self.frameLocationsList:
            if item["source_image_path"] == paths["image_path"]:
                if os.path.exists(item["resized_image_path"]):
                    cv2.putText(self.signedFrame, item["resized_image_path"].split("/")[-2], (item["start_x"]+5, item["start_y"]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    cv2.rectangle(self.signedFrame, (item["start_x"], item["start_y"]),
                                  (item["end_x"], item["end_y"]), (100, 0, 255), 2)

    def saveResizedImage(self, choice, root):
        _, height_start, height_end=self.getBaseImage()
        # print(data_path+choice.get())
        # for path in os.listdir(data_path+choice.get()):
        #     print(path)
        with open('imageNameCounter.txt', 'r', encoding='UTF-8') as file:
            counter = int(file.readline())
        with open('imageNameCounter.txt', 'w', encoding='UTF-8') as file:
            file.write(str(counter+1))
        # print(self.bbox[1], self.bbox[1]+frame_height, self.bbox[0], self.bbox[0]+frame_width)

        # with open('frameLocations.json', "r", encoding='utf-8') as file:
        #     try:
        #         self.frameLocationsList=json.load(file)
        #     except Exception as E:
        #         print(E)
        # print(self.frameLocationsList)
        frameLocation = {
            "source_image_path": paths["image_path"],
            "resized_image_path": f"{paths['image_save_path']+choice.get()}/{counter}.jpg",
            "start_x": self.bbox[0],
            "start_y": self.bbox[1]+height_start,
            "end_x": self.bbox[0]+self.frame_width,
            "end_y": self.bbox[1]+self.frame_height+height_start
        }
        self.frameLocationsList.append(frameLocation)
        with open('frameLocations.json', 'w', encoding='UTF-8') as file:
            json.dump(self.frameLocationsList, file,
                      ensure_ascii=False, indent=4)
            # file.write(f"source_image_path={path},resized_image_path={data_path+choice.get()}/{counter}.jpg,start_x={self.bbox[0]},start_y={self.bbox[1]},end_x={self.bbox[0]+frame_width},end_y={self.bbox[1]+frame_height}\n")

        cv2.rectangle(self.frame, (self.bbox[0], self.bbox[1]), (
            self.bbox[0]+self.bbox[2], self.bbox[1]+self.bbox[3]), (0, 255, 0), 1)
        cv2.putText(self.frame, choice.get(
        ), (self.bbox[0]+5, self.bbox[1]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        cv2.imwrite(f"{paths['image_save_path']+choice.get()}/{counter}.jpg", self.image)
        # cv2.destroyAllWindows()
        # takeFrameThread.kill()
        self.start()
    # print(f"{int(self.bbox[1])}:{int(self.bbox[1]+self.bbox[3])},{int(self.bbox[0])}:{int(self.bbox[0]+self.bbox[2])}")

    def takeFrame(self):
        frame, height_start, height_end=self.getBaseImage()
        self.findMarkedImages()                 
        self.bbox = cv2.selectROI(frame)
        cv2.destroyAllWindows()
        # cv2.waitKey(0)
        # self.takeFrameThread.cancel()
        # cv2.destroyAllWindows()
        if(self.bbox[2]<50 or self.bbox[3]<60):
            self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.frame_height+height_start, int(self.bbox[0]):int(self.bbox[0]+self.frame_width), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
        else:
            self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.bbox[3]+height_start, int(self.bbox[0]):int(self.bbox[0]+self.bbox[2]), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
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