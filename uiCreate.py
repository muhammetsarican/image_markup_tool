import customtkinter, keyboard, json

class UI(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("400x600+0+0")
        
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
    
    def home(self, imageself):
        self.paths_button=customtkinter.CTkButton(self, text="Edit Paths", command=self.editPaths)
        self.paths_button.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        self.combobox = customtkinter.CTkOptionMenu(master=self,
                                       values=[
                                           "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                                       )
        self.combobox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.combobox.set("0")  # set initial value

        self.submit = customtkinter.CTkButton(self, text="Save",
                                        command=lambda: imageself.saveResizedImage(self.combobox, self)
                                        )
        self.submit.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.passButton=customtkinter.CTkButton(self, text="Pass", 
                                        command=imageself.passMarking
                                        )
        self.passButton.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.errLabel = customtkinter.CTkLabel(
            self, text="After select the frame, you have to click space or enter at keyboard.\nIf you want to remark the image please push the pass button!", text_color="red")
        self.errLabel.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.exitButton=customtkinter.CTkButton(self, text="Exit", fg_color="red",
                                                command=lambda:self.exitFunction(imageself)
                                                )
        self.exitButton.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        self.switch=customtkinter.CTkSwitch(self, text="Change Image", onvalue="on", offvalue="off",
                                            command=lambda:self.changeImageFunc(imageself)
                                            )
        self.switch.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
    
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
    