from ImageSection.main import ImageSection
from UiSection.main import UI

if __name__=="__main__":
    root=UI()
    imageself = ImageSection(root)
    root.createHomePage(imageself)
    imageself.start()
    root.mainloop() 