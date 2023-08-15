from ImageSection.Libraries import os, cv2, json
def findMarkedImages(self):
    with open("./frameLocations.json", "r", encoding="utf-8") as file:
        self.frameLocationsList = json.load(file)

    for item in self.frameLocationsList:
        if item["source_image_path"] == self.getPaths()["image_path"]:
            if os.path.exists(item["resized_image_path"]):
                cv2.putText(self.signedFrame, item["resized_image_path"].split("/")[-2], (item["start_x"]+5, item["start_y"]+25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
                cv2.rectangle(self.signedFrame, (item["start_x"], item["start_y"]),
                                (item["end_x"], item["end_y"]), (0, 0, 255), 1)