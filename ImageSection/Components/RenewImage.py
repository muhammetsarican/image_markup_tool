from ImageSection.Libraries import pyautogui, cv2
def renewImage(self):
    self.frame = cv2.imread(self.getPaths()["image_path"])
    self.frame=cv2.resize(self.frame, (pyautogui.size()[1], int(pyautogui.size()[0]/2)))
    self.signedFrame=self.frame.copy()
    self.signedFrame=self.drawGrid(self.signedFrame)
    self.notSignedFrame = self.frame.copy()