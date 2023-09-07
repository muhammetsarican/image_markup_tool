from UiSection.Libraries import customtkinter
def splitTheImageParts(self, imageself, isFromImageSection):
    # heightParts=imageself.getParts()[1]
    # widthParts=imageself.getParts()[0]
    
    # self.heightVar = customtkinter.StringVar(self, "0")
    # self.widthVar = customtkinter.StringVar(self, "0")
    
    # self.widthRadioButtonList=[]
    # self.heightRadioButtonList=[]

    # if isFromImageSection:
    #     imageself.getBaseImage(self)
        
    # rowNumber=5
    # columnNumber=0
    # customtkinter.CTkLabel(self, text="Height:", text_color="white").grid(row=rowNumber, column=columnNumber, padx=10, pady=5, sticky="ew")
    # columnNumber+=1
    # for heightPart in range(heightParts):
    #     self.heightRadioButton=customtkinter.CTkRadioButton(master=self, text=f"{heightPart*self.winfo_screenheight()}-{(heightPart+1)*self.winfo_screenheight()}",
    #                                     variable=self.heightVar, value=heightPart, command=lambda:imageself.getBaseImage(self))
    #     self.heightRadioButton.grid(row=rowNumber, column=columnNumber, padx=2, pady=5, sticky="ew")
    #     self.heightRadioButtonList.append(self.heightRadioButton)
    #     columnNumber+=1
    
    # rowNumber+=1 
    # columnNumber=0
    # customtkinter.CTkLabel(self, text="Width:", text_color="white").grid(row=rowNumber, column=columnNumber, padx=10, pady=5, sticky="ew")
    # columnNumber+=1
    # for widthPart in range(widthParts):
    #     self.widthRadioButton=customtkinter.CTkRadioButton(master=self, text=f"{widthPart*self.winfo_screenwidth()}-{(widthPart+1)*self.winfo_screenwidth()}",
    #                                     variable=self.widthVar, value=widthPart, command=lambda:imageself.getBaseImage(self))
    #     self.widthRadioButton.grid(row=rowNumber, column=columnNumber, padx=2, pady=5, sticky="ew")
    #     self.widthRadioButtonList.append(self.widthRadioButton)
    #     columnNumber+=1
    
    
    heightParts=imageself.getParts()[1]
    widthParts=imageself.getParts()[0]
    
    self.heightVarList=[]
    self.widthVarList=[]


    for heightPart in range(heightParts):
        self.heightVarList.append(f"{heightPart*self.winfo_screenheight()}-{(heightPart+1)*self.winfo_screenheight()}")
    for widthPart in range(widthParts):
        self.widthVarList.append(f"{widthPart*self.winfo_screenwidth()}-{(widthPart+1)*self.winfo_screenwidth()}")
    
    self.heightVar = customtkinter.StringVar(self, self.heightVarList[0] if len(self.heightVarList)!=0 else "0")
    self.widthVar = customtkinter.StringVar(self, self.widthVarList[0] if len(self.widthVarList)!=0 else "0")
    if isFromImageSection:
        imageself.getBaseImage(self)
        self.heightVar = customtkinter.StringVar(self, self.heightVarList[0] if len(self.heightVarList)!=0 else "0")
        self.widthVar = customtkinter.StringVar(self, self.widthVarList[0] if len(self.widthVarList)!=0 else "0")

    customtkinter.CTkLabel(self, text="Height:", text_color="white").grid(row=5, column=0, padx=10, pady=5, sticky="ew")
    self.heightPartOptionMenu=customtkinter.CTkOptionMenu(self, values=self.heightVarList, variable=self.heightVar, command=imageself.getBaseImage)
    self.heightPartOptionMenu.grid(row=5, column=1, padx=10, pady=5, sticky="ew", columnspan=2)
    
    customtkinter.CTkLabel(self, text="Width:", text_color="white").grid(row=5, column=3, padx=10, pady=5, sticky="ew")
    self.widthPartOptionMenu=customtkinter.CTkOptionMenu(self, values=self.widthVarList, variable=self.widthVar, command=imageself.getBaseImage)
    self.widthPartOptionMenu.grid(row=5, column=4, padx=10, pady=5, sticky="ew", columnspan=2)
