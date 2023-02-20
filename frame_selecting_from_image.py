#
import cv2
import os
from customtkinter import CTk
import customtkinter
import json

import warnings
warnings.filterwarnings("ignore")

path="D:/OneDrive/Desktop/Resimler/KOOP Image Processing/Raw Data/2.jpeg"
data_path="D:/OneDrive/Desktop/Resimler/KOOP Image Processing/Clean Data/"

frameLocationsList=[]
# print(path[:-6])

# for path in os.listdir(path[:-6]):
#     print(path)
frame=cv2.imread(path)
notSignedFrame=frame.copy()
# frame=cv2.resize(frame,(600,600))
print(frame.shape)
frame_width=50
frame_height=60
width=frame.shape[1]
height=frame.shape[0]
frame=frame[0:int(height/2), 0:width,:]


# print(f"{int(bbox[1])}:{int(bbox[1]+bbox[3])},{int(bbox[0])}:{int(bbox[0]+bbox[2])}")
def takeFrame():
    global frameLocationsList
    bbox=cv2.selectROI(frame)
    
    image=notSignedFrame[int(bbox[1]):int(bbox[1])+frame_height,int(bbox[0]):int(bbox[0]+frame_width),:]
    cv2.imshow('Selected Image',image)
    
    # print(bbox[1], bbox[1]+frame_height, bbox[0], bbox[0]+frame_width)
    key=cv2.waitKey(0)&0xff

    if key==ord('w'):
        cv2.destroyAllWindows()
        root=CTk()
        def optionmenu_callback(choice, root, image):
            global frameLocationsList
            print(data_path+choice.get())
            # for path in os.listdir(data_path+choice.get()):
            #     print(path)
            with open('imageNameCounter.txt', 'r', encoding='UTF-8') as file:
                counter=int(file.readline())
            with open('imageNameCounter.txt', 'w', encoding='UTF-8') as file:
                file.write(str(counter+1))
            print(bbox[1], bbox[1]+frame_height, bbox[0], bbox[0]+frame_width)
            
            with open('frameLocations.json', "r", encoding='utf-8') as file:
                try:
                    frameLocationsList=json.load(file)
                except Exception as E:
                    print(E)
            # print(frameLocationsList)
            frameLocation={
                "source_image_path":path,
                "resized_image_path":f"{data_path+choice.get()}/{counter}.jpg",
                "start_x":bbox[0],
                "start_y":bbox[1],
                "end_x":bbox[0]+frame_width,
                "end_y":bbox[1]+frame_height
            }
            frameLocationsList.append(frameLocation)
            with open('frameLocations.json', 'w', encoding='UTF-8') as file:
                json.dump(frameLocationsList, file, ensure_ascii=False, indent=4)
                # file.write(f"source_image_path={path},resized_image_path={data_path+choice.get()}/{counter}.jpg,start_x={bbox[0]},start_y={bbox[1]},end_x={bbox[0]+frame_width},end_y={bbox[1]+frame_height}\n")
            
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[0]+frame_width, bbox[1]+frame_height), (0, 255, 0), 1)
            cv2.putText(frame, choice.get(), (bbox[0]+5, bbox[1]+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
            # cv2.imwrite(f"{data_path+choice.get()}/{counter}.jpg", image)
            root.destroy()

        combobox = customtkinter.CTkOptionMenu(master=root,
                                            values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                                            )
        combobox.pack(padx=20, pady=10)
        combobox.set("0")  # set initial value
        
        submit=customtkinter.CTkButton(root, text="Save", command=lambda:optionmenu_callback(combobox, root, image))
        submit.pack(padx=20, pady=20)
        
        err_label=customtkinter.CTkLabel(root, text="Err_Label")
        err_label.pack(padx=20, pady=40)
        root.mainloop()
        takeFrame()
    if key==ord('q'):
        cv2.destroyAllWindows()
takeFrame()