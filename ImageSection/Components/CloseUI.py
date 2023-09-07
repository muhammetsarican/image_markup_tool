from ImageSection.Libraries import cv2, pyautogui
def closeUI(self):
    # try:
    #     if self.bbox:
    #         pass
    # except:
    #     keyboard.press_and_release("c")

    r_frame=cv2.resize(self.signedFrame, (pyautogui.size()[0]-100, pyautogui.size()[1]-100))
    # cv2.imshow("frame", r_frame)
    cv2.waitKey(0)