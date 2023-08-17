import customtkinter
from UiSection.Libraries import *

class UI(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry(f"700x{self.winfo_screenheight()-50}+0+0")
        
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    
    def changeDefaultClass(self, choice=True):
        return ChangeDefaultClass.changeDefaultClass(self, choice)
        
    def changeButtonStateToNormal(self):
        return ChangeButtonState.changeButtonStateToNormal(self)

    def changeButtonStateToDisabled(self):
        return ChangeButtonState.changeButtonStateToDisabled(self) 

    def createHomePage(self, imageself):
        return CreateHomePage.createHomePage(self, imageself)
    
    def splitTheImageParts(self, imageself, isFromImageSection=False):
        return SplitTheImageParts.splitTheImageParts(self, imageself, isFromImageSection)
            
            
    def changeImageFunc(self, imageself):
        if not imageself.upsideORdownside:
            imageself.upsideORdownside=True
        else:
            imageself.upsideORdownside=False
            
    def editPaths(self):
        return EditPathsDialog.editPaths(self)
        
    def exitFunction(self, imageself):
        self.destroy()
        imageself.closeUI()
    