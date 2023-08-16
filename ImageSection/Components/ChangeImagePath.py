from ImageSection.Libraries import json, os
def changeImagePath(self, path):
    # isFileFound=False
    # newFileName=""
    # slashIndex=0

    paths={}
    with open("filePath.json", "r", encoding="utf-8") as file:
        paths=(json.load(file))
    # slashIndex=str(paths["win_path"]["image_path"]).rfind("/")+1

    # for file in os.listdir(paths["win_path"]["image_path"][0:slashIndex]):
    #     if isFileFound:
    #         newFileName=file
    #         break
    #     if file==paths["win_path"]["image_path"][slashIndex:]:
    #         isFileFound=True

    paths["win_path"]["image_path"]=path
    # paths["win_path"]["image_path"]=path
    print("new path:"+path)
    with open("filePath.json", "w", encoding="utf-8") as file:
        json.dump(paths, file, indent=4)
    self.renewImage()