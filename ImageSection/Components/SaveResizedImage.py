from ImageSection.Libraries import *
def saveDataAboutResizedImages(self, choice):
        _, height_start, height_end, width_start, width_end=self.getBaseImage()
        # with open('frameLocations.json', 'w', encoding='UTF-8') as file:
        #     frameLocation=json.load(file)
        # if frameLocation[0]["source_image_path"]==self.getPaths()["image_path"]:
        #     frameLocation[0]["info"].append(                
        #         {                
        #             "resized_image_path": f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg",
        #             "start_x": self.bbox[0]+width_start,
        #             "start_y": self.bbox[1]+height_start,
        #             "end_x": self.bbox[0]+self.bbox[2]+width_start,
        #             "end_y": self.bbox[1]+self.bbox[3]+height_start
        #         }
        # else:                
        #     frameLocation.append( 
        #         {
        #             "source_image_path": self.getPaths()["image_path"],
        #             "info":[
        #                 {                
        #                     "resized_image_path": f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg",
        #                     "start_x": self.bbox[0]+width_start,
        #                     "start_y": self.bbox[1]+height_start,
        #                     "end_x": self.bbox[0]+self.bbox[2]+width_start,
        #                     "end_y": self.bbox[1]+self.bbox[3]+height_start
        #                 }
        #             ]
        #         }
        #     )

        if self.frameLocationsList[0]["source_image_path"]==self.getPaths()["image_path"]:
            self.frameLocationsList["info"].append(                
                {                
                    "resized_image_path": f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg",
                    "start_x": self.bbox[0]+width_start,
                    "start_y": self.bbox[1]+height_start,
                    "end_x": self.bbox[0]+self.bbox[2]+width_start,
                    "end_y": self.bbox[1]+self.bbox[3]+height_start
                }
            )
        else:                
            self.frameLocationsList.append( 
                {
                    "source_image_path": self.getPaths()["image_path"],
                    "info":[
                        {                
                            "resized_image_path": f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg",
                            "start_x": self.bbox[0]+width_start,
                            "start_y": self.bbox[1]+height_start,
                            "end_x": self.bbox[0]+self.bbox[2]+width_start,
                            "end_y": self.bbox[1]+self.bbox[3]+height_start
                        }
                    ]
                }
            )
        # self.frameLocationsList.append(frameLocation)
        with open('frameLocations.json', 'w', encoding='UTF-8') as file:
            json.dump(self.frameLocationsList, file,
                    ensure_ascii=False, indent=4)
def saveResizedImage(self, choice, root, changeTheImage):
    if self.image is not None:
        # saveDataAboutResizedImages(self, choice)
        _, height_start, height_end, width_start, width_end=self.getBaseImage()
        
        frameLocation = {
            "source_image_path": self.getPaths()["image_path"],
            "resized_image_path": f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg",
            "start_x": self.bbox[0]+width_start,
            "start_y": self.bbox[1]+height_start,
            "end_x": self.bbox[0]+self.bbox[2]+width_start,
            "end_y": self.bbox[1]+self.bbox[3]+height_start
        }
        self.frameLocationsList.append(frameLocation)
        with open('frameLocations.json', 'w', encoding='UTF-8') as file:
            json.dump(self.frameLocationsList, file,
                    ensure_ascii=False, indent=4)
        # print(data_path+choice.get())
        # for path in os.listdir(data_path+choice.get()):
        #     print(path)
        # print(self.bbox[1], self.bbox[1]+frame_height, self.bbox[0], self.bbox[0]+frame_width)

        # with open('frameLocations.json', "r", encoding='utf-8') as file:
        #     try:
        #         self.frameLocationsList=json.load(file)
        #     except Exception as E:
        #         print(E)
        # print(self.frameLocationsList)

            # file.write(f"source_image_path={path},resized_image_path={data_path+choice.get()}/{self.fileCounter()}.jpg,start_x={self.bbox[0]},start_y={self.bbox[1]},end_x={self.bbox[0]+frame_width},end_y={self.bbox[1]+frame_height}\n")

        # cv2.rectangle(self.frame, (self.bbox[0], self.bbox[1]), (
        #     self.bbox[0]+self.bbox[2], self.bbox[1]+self.bbox[3]), (0, 255, 0), 1)
        # cv2.putText(self.frame, choice.get(
        # ), (self.bbox[0]+5, self.bbox[1]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        cv2.imwrite(f"{self.getPaths()['image_save_path']+choice.get()}/{self.getLastImageCount(choice.get()) or self.fileCounter()}.jpg", self.image)
        self.getSignedPictureCount(choice.get())
        # cv2.destroyAllWindows()
        # takeFrameThread.kill()
        self.changeImagePath(changeTheImage)
        self.start()
    # print(f"{int(self.bbox[1])}:{int(self.bbox[1]+self.bbox[3])},{int(self.bbox[0])}:{int(self.bbox[0]+self.bbox[2])}")
    else: 
        print("[INFO]-Saving process passed.")
        self.start()
        
        pass