from UiSection.Libraries import customtkinter
def splitTheImageParts(self, imageself, isFromImageSection):
    heightParts=imageself.getParts()[1]
    widthParts=imageself.getParts()[0]
    
    self.heightVar = customtkinter.IntVar(self, 0)
    self.widthVar = customtkinter.IntVar(self, 0)
    
    self.widthRadioButtonList=[]
    self.heightRadioButtonList=[]

    if isFromImageSection:
        imageself.getBaseImage(self)
        
    rowNumber=5
    columnNumber=0
    customtkinter.CTkLabel(self, text="Height:", text_color="white").grid(row=rowNumber, column=columnNumber, padx=10, pady=5, sticky="ew")
    columnNumber+=1
    for heightPart in range(heightParts):
        self.heightRadioButton=customtkinter.CTkRadioButton(master=self, text=f"{heightPart*self.winfo_screenheight()}-{(heightPart+1)*self.winfo_screenheight()}",
                                        variable=self.heightVar, value=heightPart, command=lambda:imageself.getBaseImage(self))
        self.heightRadioButton.grid(row=rowNumber, column=columnNumber, padx=2, pady=5, sticky="ew")
        self.heightRadioButtonList.append(self.heightRadioButton)
        columnNumber+=1
    
    rowNumber+=1 
    columnNumber=0
    customtkinter.CTkLabel(self, text="Width:", text_color="white").grid(row=rowNumber, column=columnNumber, padx=10, pady=5, sticky="ew")
    columnNumber+=1
    for widthPart in range(widthParts):
        self.widthRadioButton=customtkinter.CTkRadioButton(master=self, text=f"{widthPart*self.winfo_screenwidth()}-{(widthPart+1)*self.winfo_screenwidth()}",
                                        variable=self.widthVar, value=widthPart, command=lambda:imageself.getBaseImage(self))
        self.widthRadioButton.grid(row=rowNumber, column=columnNumber, padx=2, pady=5, sticky="ew")
        self.widthRadioButtonList.append(self.widthRadioButton)
        columnNumber+=1