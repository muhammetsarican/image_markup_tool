import cv2, os, json, keyboard
from threading import Thread
import pyautogui

class ImageSection:
    def __init__(self):
        print("Get Paths:",self.getPaths()["image_path"])
    def getPaths(self):
        with open("filePath.json", "r", encoding="utf-8") as file:
             path=json.load(file)
        return path["win_path"]
    def getSignedPictureCount(self, choice):
        path=self.getPaths()["image_save_path"]+choice
        print("Signed image count is ",len(os.listdir(path)))
        return str(len(os.listdir(path))) if bool(len(os.listdir(path))) is not None else "Null"
        
    def drawGrid(self, frame):
        if self is None:
            pass
        # else:
        #     self.getSignedPictureCount(None)
        step=20
        for width in range(0, frame.shape[0], step):
            frame=cv2.line(frame, (0, width), (frame.shape[1],width), (0,100,0), 1)
        for height in range(0, frame.shape[1], step):   
            frame=cv2.line(frame, (height,frame.shape[0]), (height,0), (0,100,0), 1)
            
        return frame

    def renewImage(self):
        self.frame = cv2.imread(self.getPaths()["image_path"])
        self.frame=cv2.resize(self.frame, (pyautogui.size()[1], int(pyautogui.size()[0]/2)))
        self.signedFrame=self.frame.copy()
        self.signedFrame=self.drawGrid(self.signedFrame)
        self.notSignedFrame = self.frame.copy()
        
    frame=cv2.imread(getPaths(None)["image_path"])
    frame=cv2.resize(frame, (pyautogui.size()[1], int(pyautogui.size()[0]/2)))
    
    isUiFirstLoad = True
    frameLocationsList = []
    # frame=cv2.resize(frame, None, fx=0, fy=0)

    signedFrame=frame.copy()
    signedFrame=drawGrid(None, signedFrame)
    notSignedFrame = frame.copy()
    
    # frame=cv2.resize(frame,(600,600))
    # print(frame.shape)
    frame_width = 128
    frame_height = 128
    width = frame.shape[1]
    height = frame.shape[0]
        
    upsideORdownside=True
    width_start=0
    height_start=0  
    
    passedImageCount=0
    
    def getParts(self):
        return int(self.frame.shape[1]/pyautogui.size()[0]), int(self.frame.shape[0]/pyautogui.size()[1])# It sends width first, height second
    
    def fileCounter(self):
        fileCounter=0
        for path in os.listdir(self.getPaths()["image_save_path"]):
            for _ in os.listdir(self.getPaths()["image_save_path"]+path):
                fileCounter+=1
        return fileCounter+1

    def getLastImageCount(self, choice):
        maxImgCount=0
        for imgName in os.listdir(self.getPaths()["image_save_path"]+choice):
            if int(imgName[:-4])>maxImgCount:
                maxImgCount=int(imgName[:-4])
        return maxImgCount+1
    
    def radiobutton_event(self, ui):
        print("Height radiobutton toggled, current value:", ui.heightVar.get())
        print("Width radiobutton toggled, current value:", ui.widthVar.get())
    
    def getBaseImage(self, ui=None):
        if ui is not None:
            self.width_start=ui.widthVar.get()*pyautogui.size()[0]
            self.height_start=ui.heightVar.get()*pyautogui.size()[1]
            print(f"Ui: {self.width_start, self.height_start}")
        
        width_end=self.width_start+pyautogui.size()[0]
        height_end=self.height_start+pyautogui.size()[1]

        frame = self.signedFrame[self.height_start:height_end, self.width_start:width_end, :]
        return frame, self.height_start, height_end, self.width_start, width_end

    def start(self):
        self.takeFrameThread = Thread(target=self.takeFrame, args=())
        self.takeFrameThread.daemon=True
        self.takeFrameThread.start()
        
    def findMarkedImages(self):
        with open("./frameLocations.json", "r", encoding="utf-8") as file:
            self.frameLocationsList = json.load(file)

        for item in self.frameLocationsList:
            if item["source_image_path"] == self.getPaths()["image_path"]:
                if os.path.exists(item["resized_image_path"]):
                    cv2.putText(self.signedFrame, item["resized_image_path"].split("/")[-2], (item["start_x"]+5, item["start_y"]+25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
                    cv2.rectangle(self.signedFrame, (item["start_x"], item["start_y"]),
                                  (item["end_x"], item["end_y"]), (0, 0, 255), 1)
                    
    def changeImagePath(self):
        isFileFound=False
        newFileName=""
        slashIndex=0

        paths={}
        with open("filePath.json", "r", encoding="utf-8") as file:
            paths=(json.load(file))
        slashIndex=str(paths["win_path"]["image_path"]).rfind("/")+1

        for file in os.listdir(paths["win_path"]["image_path"][0:slashIndex]):
            if isFileFound:
                newFileName=file
                break
            if file==paths["win_path"]["image_path"][slashIndex:]:
                isFileFound=True

        paths["win_path"]["image_path"]=str(paths["win_path"]["image_path"]).replace(paths["win_path"]["image_path"][slashIndex:], newFileName)
        print("new path:"+paths["win_path"]["image_path"])
        with open("filePath.json", "w", encoding="utf-8") as file:
            json.dump(paths, file, indent=4)
        self.renewImage()

    def saveResizedImage(self, choice, root, changeTheImage=True):
        if self.image is not None:
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
                "source_image_path": self.getPaths()["image_path"],
                "resized_image_path": f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg",
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
            cv2.imwrite(f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg", self.image)
            self.getSignedPictureCount(choice.get())
            # cv2.destroyAllWindows()
            # takeFrameThread.kill()
            if changeTheImage:
                self.changeImagePath()
            self.start()
        # print(f"{int(self.bbox[1])}:{int(self.bbox[1]+self.bbox[3])},{int(self.bbox[0])}:{int(self.bbox[0]+self.bbox[2])}")
        else:
            pass
            
    def takeFrame(self):
        passValue=False
        frame, height_start, height_end, width_start, width_end=self.getBaseImage()
        self.findMarkedImages()                 
        self.bbox = cv2.selectROI(frame)
        cv2.destroyAllWindows()
        passValue=True if self.bbox[0]<5 and self.bbox[1]<5 and self.bbox[2]<5 and self.bbox[3]<5 else False
        if passValue:
            self.image=None
        else:
            self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.bbox[3]+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+self.bbox[2]+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
            self.image=cv2.resize(self.image, (self.frame_width, self.frame_height))
        # cv2.waitKey(0)
        # self.takeFrameThread.cancel()
        # cv2.destroyAllWindows()
        # if(self.bbox[2]<128 or self.bbox[3]<128):
        #     # if(self.bbox[2]+passValue>128 or self.bbox[3]+passValue>128):
        #     # self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.frame_height+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+self.frame_width+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
        #     # self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+(self.bbox[3]+passValue)+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+(self.bbox[2]+passValue)+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
        #     self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.bbox[3]+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+self.bbox[2]+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
        #     self.image=cv2.resize(self.image, (self.frame_width, self.frame_height))

        #     # else:    
        #     self.passedImageCount+=1
        #     print("Passed image count: ",self.passedImageCount)
        #     # self.image=None
        # else:
        #     self.image = self.notSignedFrame[int(self.bbox[1])+height_start:int(self.bbox[1])+self.bbox[3]+height_start, int(self.bbox[0])+width_start:int(self.bbox[0]+self.bbox[2]+width_start), :] # here I added the height_start because if I want to take downside of photo I have to add this but if I dont do this resized image will be upside of photo
        #     self.image=cv2.resize(self.image, (self.frame_width, self.frame_height))
        # cv2.imshow("notSignedFrame", self.image)
        # cv2.waitKey(0)
        
    def passMarking(self):
        # cv2.destroyWindow("notSignedFrame")
        self.changeImagePath()
        self.start()
        
    def remarkTheImage(self):
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