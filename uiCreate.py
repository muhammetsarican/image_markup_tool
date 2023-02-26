import customtkinter

class UI(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def home(self, imageself):
        self.combobox = customtkinter.CTkOptionMenu(master=self,
                                       values=[
                                           "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                                       )
        self.combobox.pack(padx=20, pady=10)
        self.combobox.set("0")  # set initial value

        self.submit = customtkinter.CTkButton(self, text="Save",
                                        command=lambda: imageself.saveResizedImage(self.combobox, self)
                                        )
        self.submit.pack(padx=20, pady=20)

        self.passButton=customtkinter.CTkButton(self, text="Pass", 
                                        command=imageself.passMarking
                                        )
        self.passButton.pack(padx=10, pady=20)
        self.errLabel = customtkinter.CTkLabel(
            self, text="After select the frame,\nyou have to click space or enter at keyboard\nIf you want to remark the image\nplease push the pass button!", text_color="red")
        self.errLabel.pack(padx=20, pady=40)
        