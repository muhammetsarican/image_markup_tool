from UiSection.Libraries import customtkinter
def splitTheImageParts(self, imageself):
    heightParts=imageself.getParts()[1]
    widthParts=imageself.getParts()[0]
    
    self.heightVar = customtkinter.IntVar(self, 0)
    self.widthVar = customtkinter.IntVar(self, 0)

    rowNumber=5
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