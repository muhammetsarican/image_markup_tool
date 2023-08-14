import customtkinter, keyboard, json

class UI(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry(f"700x{self.winfo_screenheight()-50}+0+0")
        
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    
    def changeDefaultClass(self, choice=True):
        defaultClass=""
        if choice:
            with open("./defaultClass.txt", "w")as file:
                file.write(self.combobox.get())
        else:
            try:
                with open("./defaultClass.txt", "r")as file:
                    defaultClass=str(file.readline()).strip("\n")
            except:
                with open("./defaultClass.txt", "w")as file:
                    file.write(self.combobox.get())
                    self.changeDefaultClass()
            return defaultClass
    def home(self, imageself):
        self.paths_button=customtkinter.CTkButton(self, text="Edit Paths", command=self.editPaths)
        self.paths_button.grid(row=0, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
        
        self.combobox = customtkinter.CTkOptionMenu(master=self,
                                    values=[
                                        "0","1", "2", "3", "4", "5", "6", "7", "8", "9"], command=self.changeDefaultClass
                                    )
        self.combobox.grid(row=1, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
        self.combobox.set(self.changeDefaultClass(False))  # set initial value

        self.submit = customtkinter.CTkButton(self, text=f"Save and next image", fg_color="green",
                                        command=lambda: imageself.saveResizedImage(self.combobox, self), state="disabled", text_color_disabled="gray", 
                                        )
        self.submit.grid(row=2, column=0, padx=10, pady=5, sticky="ew", columnspan=2)

        self.markOnTheSameImage=customtkinter.CTkButton(self, text="Save and same image", fg_color="brown", text_color="white", command=lambda: imageself.saveResizedImage(self.combobox, self, False))
        self.markOnTheSameImage.grid(row=2, column=2, padx=10, pady=5, sticky="ew", columnspan=2)
        
        self.remarkButton=customtkinter.CTkButton(self, text="Re-mark the image", fg_color="purple", text_color="white", command=imageself.remarkTheImage)
        self.remarkButton.grid(row=2, column=4, padx=10, pady=5, sticky="ew")
        
        self.passButton=customtkinter.CTkButton(self, text="Pass", fg_color="orange", text_color="black",
                                        command=imageself.passMarking
                                        )
        self.passButton.grid(row=2, column=5, padx=10, pady=5, sticky="ew", columnspan=2)
        
        self.errLabel = customtkinter.CTkLabel(
            self, text="After select the frame, you have to click space or enter at keyboard.\nIf you want to remark the image please push the pass button!", text_color="red")
        self.errLabel.grid(row=3, column=0, columnspan=6, padx=10, pady=5, sticky="ew")

        self.exitButton=customtkinter.CTkButton(self, text="Exit", fg_color="red",
                                                command=lambda:self.exitFunction(imageself)
                                                )
        self.exitButton.grid(row=6, column=5, padx=10, pady=5, sticky="ew")
        
        self.addScreenPart(imageself)
        # self.switch=customtkinter.CTkSwitch(self, text="Change Image", onvalue="on", offvalue="off",
        #                                     command=lambda:self.changeImageFunc(imageself)
        #                                     )
        # self.switch.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
    def addScreenPart(self, imageself):
        heightParts=imageself.getParts()[1]
        widthParts=imageself.getParts()[0]
        
        self.heightVar = customtkinter.IntVar(self, 0)
        self.widthVar = customtkinter.IntVar(self, 0)

        rowNumber=4
        columnNumber=0
        customtkinter.CTkLabel(self, text="Height:", text_color="white").grid(row=rowNumber, column=columnNumber, padx=10, pady=5, sticky="ew")
        columnNumber+=1
        for heightPart in range(heightParts):
            customtkinter.CTkRadioButton(master=self, text=f"{heightPart*self.winfo_screenheight()}-{(heightPart+1)*self.winfo_screenheight()}",
                                            variable=self.heightVar, value=heightPart, command=lambda:imageself.getBaseImage(self)).grid(row=rowNumber, column=columnNumber, padx=2, pady=5, sticky="ew")
            columnNumber+=1
        
        rowNumber+=1 
        columnNumber=0
        customtkinter.CTkLabel(self, text="Width:", text_color="white").grid(row=rowNumber, column=columnNumber, padx=10, pady=5, sticky="ew")
        columnNumber+=1
        for widthPart in range(widthParts):
            customtkinter.CTkRadioButton(master=self, text=f"{widthPart*self.winfo_screenwidth()}-{(widthPart+1)*self.winfo_screenwidth()}",
                                            variable=self.widthVar, value=widthPart, command=lambda:imageself.getBaseImage(self)).grid(row=rowNumber, column=columnNumber, padx=2, pady=5, sticky="ew")
            columnNumber+=1

            
            
    def changeImageFunc(self, imageself):
        if not imageself.upsideORdownside:
            imageself.upsideORdownside=True
        else:
            imageself.upsideORdownside=False
            
    def editPaths(self):
        with open("filePath.json", "r", encoding="utf-8") as file:
            paths=json.load(file)
        path=paths["win_path"]
        def destroyDialog():
            self.path_dialog.destroy()
            
        def savePaths():
            paths["win_path"]["image_path"]=self.image_data_path.get()
            paths["win_path"]["image_save_path"]=self.image_save_path.get()
            with open("filePath.json", "w", encoding="utf-8") as file:
                json.dump(paths, file, ensure_ascii=False, indent=4)
            destroyDialog()
            
        self.path_dialog=customtkinter.CTkInputDialog(text="")
        self.path_dialog.geometry("500x350")     
        
        self.label=customtkinter.CTkLabel(self.path_dialog, text="Image Path")
        self.label.pack(padx=0, pady=0)
        
        self.image_data_path=customtkinter.CTkEntry(self.path_dialog, width=450)
        self.image_data_path.pack(padx=20, pady=0)
        
        self.image_data_path.insert(0, path["image_path"])

        self.data_label=customtkinter.CTkLabel(self.path_dialog, text="Data Path")
        self.data_label.pack(padx=0, pady=10)

        self.image_save_path=customtkinter.CTkEntry(self.path_dialog, width=450)
        self.image_save_path.pack(padx=20, pady=10)
        
        self.image_save_path.insert(0, path["image_save_path"])
        
        self.save=customtkinter.CTkButton(self.path_dialog, text="Save", command=savePaths)
        self.save.pack(padx=0, pady=20)
        
        self.exit=customtkinter.CTkButton(self.path_dialog, text="Exit", command=destroyDialog)
        self.exit.pack(padx=20, pady=20)
        
    def exitFunction(self, imageself):
        self.destroy()
        imageself.closeUI()
    