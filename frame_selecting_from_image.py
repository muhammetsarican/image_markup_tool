from threading import Thread

from ImageSection import ImageSection
from uiCreate import UI

imageself = ImageSection()
takeFrameThread = Thread(target=imageself.takeFrame, args=())

root=UI()
takeFrameThread.start()
root.home(imageself)
root.mainloop()