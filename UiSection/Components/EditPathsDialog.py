from UiSection.Libraries import customtkinter, json
def editPaths(self):
    with open("./filePath.json", "r", encoding="utf-8") as file:
        paths=json.load(file)
    path=paths["win_path"]
    def destroyDialog():
        self.path_dialog.destroy()
        
    def savePaths():
        paths["win_path"]["image_path"]=self.image_data_path.get()
        paths["win_path"]["image_save_path"]=self.image_save_path.get()
        with open("./filePath.json", "w", encoding="utf-8") as file:
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