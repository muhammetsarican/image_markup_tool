from UiSection.Libraries import customtkinter
def createHomePage(self, imageself):
    self.paths_button=customtkinter.CTkButton(self, text="Edit Paths", command=self.editPaths)
    self.paths_button.grid(row=0, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
    
    self.combobox = customtkinter.CTkOptionMenu(master=self,
                                values=[
                                    "0","1", "2", "3", "4", "5", "6", "7", "8", "9"], command=self.changeDefaultClass
                                )
    self.combobox.grid(row=1, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
    self.combobox.set(self.changeDefaultClass(False))  # set initial value

    self.saveAndSkipNextImage = customtkinter.CTkButton(self, text=f"Save and skip next image", fg_color="green",
                                    command=lambda: imageself.saveResizedImage(self.combobox, self, True)
                                    )
    self.saveAndSkipNextImage.grid(row=2, column=0, padx=10, pady=5, sticky="ew", columnspan=2)

    self.saveAndStaySameImage=customtkinter.CTkButton(self, text="Save and stay same image", fg_color="brown", text_color="white", command=lambda: imageself.saveResizedImage(self.combobox, self, None))
    self.saveAndStaySameImage.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
    
    self.remarkButton=customtkinter.CTkButton(self, text="Re-mark", fg_color="purple", text_color="white", command=imageself.remarkTheImage)
    self.remarkButton.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
    
    self.passButton=customtkinter.CTkButton(self, text="Pass", fg_color="orange", text_color="black",
                                    command=imageself.passMarking
                                    )
    self.passButton.grid(row=2, column=4, padx=10, pady=5, sticky="ew")

    self.passNextImage=customtkinter.CTkButton(self, text="Next", fg_color="black", text_color="white", command=lambda:imageself.changeImageWithPrevOrNext(True))
    self.passNextImage.grid(row=3, column=0, padx=10, pady=5, sticky="ew", columnspan=3)
    
    self.returnPrevImage=customtkinter.CTkButton(self, text="Prev", fg_color="white", text_color="black", command=lambda:imageself.changeImageWithPrevOrNext(False))
    self.returnPrevImage.grid(row=3, column=3, padx=10, pady=5, sticky="ew", columnspan=3)
    
    self.errLabel = customtkinter.CTkLabel(
        self, text="After select the frame, you have to click space or enter at keyboard.\nIf you want to remark the image please push the pass button!", text_color="red")
    self.errLabel.grid(row=4, column=0, columnspan=6, padx=10, pady=5, sticky="ew")

    self.splitTheImageParts(imageself)
    
    self.developerInfo=customtkinter.CTkLabel(self, text="Developed by muhammetsarican", text_color="white", height=36)
    self.developerInfo.grid(row=6, column=0, padx=10, pady=1, sticky="ew", columnspan=6)

    self.exitButton=customtkinter.CTkButton(self, text="Exit", fg_color="red",
                                            command=lambda:self.exitFunction(imageself)
                                            )
    self.exitButton.grid(row=7, column=0, padx=10, pady=2, sticky="ew", columnspan=6)
    # self.switch=customtkinter.CTkSwitch(self, text="Change Image", onvalue="on", offvalue="off",
    #                                     command=lambda:self.changeImageFunc(imageself)
    #                                     )
    # self.switch.grid(row=4, column=0, padx=10, pady=5, sticky="ew")