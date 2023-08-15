from ImageSection.Libraries import os
def getSignedPictureCount(self, choice):
    path=self.getPaths()["image_save_path"]+choice
    print("Signed image count is ",len(os.listdir(path)))
    return str(len(os.listdir(path))) if bool(len(os.listdir(path))) is not None else "Null"