from ImageSection.Libraries import cv2

def takeFrame(self):
    self.ui.changeButtonStateToDisabled()
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
    self.ui.changeButtonStateToNormal()
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
