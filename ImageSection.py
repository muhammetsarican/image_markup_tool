import cv2, os, json

path = "D:/OneDrive/Desktop/Resimler/KOOP Image Processing/Raw Data/2.jpeg"
data_path = "D:/OneDrive/Desktop/Resimler/KOOP Image Processing/Clean Data/"

class ImageSection:
    isUiFirstLoad = True
    frameLocationsList = []
    
    frame = cv2.imread(path)

    notSignedFrame = frame.copy()
    # frame=cv2.resize(frame,(600,600))
    # print(frame.shape)
    frame_width = 50
    frame_height = 60
    width = frame.shape[1]
    height = frame.shape[0]
    frame = frame[0:int(height/2), 0:width, :]

    def __init__(self) -> None:
        pass

    def findMarkedImages(self):
        with open("frameLocations.json", "r", encoding="utf-8") as file:
            self.frameLocationsList = json.load(file)

        for item in self.frameLocationsList:
            if item["source_image_path"] == path:
                if os.path.exists(item["resized_image_path"]):
                    cv2.putText(self.frame, item["resized_image_path"].split(
                        "/")[-2], (item["start_x"]+5, item["start_y"]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.rectangle(self.frame, (item["start_x"], item["start_y"]),
                                  (item["end_x"], item["end_y"]), (0, 0, 255), 2)

    def saveResizedImage(self, choice, root):
        # print(data_path+choice.get())
        # for path in os.listdir(data_path+choice.get()):
        #     print(path)
        with open('imageNameCounter.txt', 'r', encoding='UTF-8') as file:
            counter = int(file.readline())
        with open('imageNameCounter.txt', 'w', encoding='UTF-8') as file:
            file.write(str(counter+1))
        # print(self.bbox[1], self.bbox[1]+frame_height, self.bbox[0], self.bbox[0]+frame_width)

        # with open('frameLocations.json', "r", encoding='utf-8') as file:
        #     try:
        #         self.frameLocationsList=json.load(file)
        #     except Exception as E:
        #         print(E)
        # print(self.frameLocationsList)
        frameLocation = {
            "source_image_path": path,
            "resized_image_path": f"{data_path+choice.get()}/{counter}.jpg",
            "start_x": self.bbox[0],
            "start_y": self.bbox[1],
            "end_x": self.bbox[0]+self.frame_width,
            "end_y": self.bbox[1]+self.frame_height
        }
        self.frameLocationsList.append(frameLocation)
        with open('frameLocations.json', 'w', encoding='UTF-8') as file:
            json.dump(self.frameLocationsList, file,
                      ensure_ascii=False, indent=4)
            # file.write(f"source_image_path={path},resized_image_path={data_path+choice.get()}/{counter}.jpg,start_x={self.bbox[0]},start_y={self.bbox[1]},end_x={self.bbox[0]+frame_width},end_y={self.bbox[1]+frame_height}\n")

        cv2.rectangle(self.frame, (self.bbox[0], self.bbox[1]), (
            self.bbox[0]+self.frame_width, self.bbox[1]+self.frame_height), (0, 255, 0), 1)
        cv2.putText(self.frame, choice.get(
        ), (self.bbox[0]+5, self.bbox[1]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        cv2.imwrite(f"{data_path+choice.get()}/{counter}.jpg", self.image)
        # cv2.destroyAllWindows()
        # takeFrameThread.kill()
        self.takeFrame()
    # print(f"{int(self.bbox[1])}:{int(self.bbox[1]+self.bbox[3])},{int(self.bbox[0])}:{int(self.bbox[0]+self.bbox[2])}")

    def takeFrame(self):

        self.findMarkedImages()
        self.bbox = cv2.selectROI(self.frame)

        self.image = self.notSignedFrame[int(self.bbox[1]):int(
            self.bbox[1])+self.frame_height, int(self.bbox[0]):int(self.bbox[0]+self.frame_width), :]

        cv2.destroyAllWindows()
        self.isUiFirstLoad = True
        # print(bbox[1], bbox[1]+frame_height, bbox[0], bbox[0]+frame_width)
        key = cv2.waitKey(0) & 0xff

        if key == ord('q'):
            cv2.destroyAllWindows()
    
    def passMarking(self):
        self.takeFrame()