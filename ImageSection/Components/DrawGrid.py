from ImageSection.Libraries import cv2
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