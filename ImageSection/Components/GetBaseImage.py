from ImageSection.Libraries import pyautogui
def getBaseImage(self, ui=None):
    print("[Info]_Get base image is working")
    if ui is not None:
        print("[Info]_ui is exist")
        self.width_start=ui.widthVar.get()*pyautogui.size()[0]
        self.height_start=ui.heightVar.get()*pyautogui.size()[1]
        print(f"Ui: {self.width_start, self.height_start}")
        self.start()
    
    width_end=self.width_start+pyautogui.size()[0]
    height_end=self.height_start+pyautogui.size()[1]

    frame = self.signedFrame[self.height_start:height_end, self.width_start:width_end, :]
    return frame, self.height_start, height_end, self.width_start, width_end