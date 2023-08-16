from ImageSection.Libraries import *
class ImageSection:
    def __init__(self, ui):
        self.ui=ui
        print("Get Paths:",self.getPaths()["image_path"])
     
    def getPaths(self):
        with open("filePath.json", "r", encoding="utf-8") as file:
             path=json.load(file)
        return path["win_path"] 
      
    def drawGrid(self, frame):
        return DrawGrid.drawGrid(self, frame)
    
    frame=cv2.imread(getPaths(None)["image_path"])
    # frame=cv2.resize(frame, (pyautogui.size()[1], int(pyautogui.size()[0]/2)))
    
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

    def getSignedPictureCount(self, choice):
        return GetSignedPictureCount.getSignedPictureCount(self, choice)
    
    def renewImage(self):
        return RenewImage.renewImage(self)
    
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
        return GetBaseImage.getBaseImage(self, ui)

    def start(self):
        self.takeFrameThread = Thread(target=self.takeFrame, args=())
        self.takeFrameThread.daemon=True
        self.takeFrameThread.start()
        
    def findMarkedImages(self):
        return FindMarkedImages.findMarkedImages(self)
    
    def getRawImages(self):
        rawImagePath=None
        with open("./filePath.json", "r", encoding="utf-8") as file:
            rawImagePath=json.load(file)  
        return rawImagePath["win_path"]["image_path"][:rawImagePath["win_path"]["image_path"].rfind("/")+1], os.listdir(rawImagePath["win_path"]["image_path"][:rawImagePath["win_path"]["image_path"].rfind("/")+1])
            
    def getPrevOrNextImage(self, isPrevOrNext):
        path, imageName=self.getRawImages()    
        for index, image in enumerate(imageName):
            if path+image==self.getPaths()["image_path"]:
                print(path+image, index)
                # print(imageName)
                if isPrevOrNext is None:
                    return path+imageName[index] 
                else:
                    if index>=0 and index<=len(imageName):
                        if isPrevOrNext:
                            return path+imageName[index+1] 
                        else:
                            return path+imageName[index-1] 
                    else:
                        print("[Info]_You reached first or last image.")
                        return path+imageName[index] 
                # return path+imageName[index] if isPrevOrNext is None else path+imageName[index+1] if isPrevOrNext else path+imageName[index-1]
            
    def changeImagePath(self, isPrevOrNext=None):
        path=self.getPrevOrNextImage(isPrevOrNext)
        return ChangeImagePath.changeImagePath(self, path)

    def saveResizedImage(self, choice, root, changeTheImage=True):
        return SaveResizedImage.saveResizedImage(self, choice, root, changeTheImage)
            
    def takeFrame(self):
        return TakeFrame.takeFrame(self)
    
    def passMarking(self):
        # cv2.destroyWindow("notSignedFrame")
        # self.changeImagePath(True)
        self.start()
        
    def remarkTheImage(self):
        self.start()
        
    def changeImageWithPrevOrNext(self, isChange):
        self.changeImagePath() if isChange is None else self.changeImagePath(True) if isChange else self.changeImagePath(False)
        self.start()
        
    def closeUI(self):
        return CloseUI.closeUI(self)