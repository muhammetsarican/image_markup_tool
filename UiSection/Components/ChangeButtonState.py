def changeButtonStateToNormal(self):
        self.paths_button.configure(state="normal")   
        self.saveAndSkipNextImage.configure(state="normal")   
        self.saveAndStaySameImage.configure(state="normal")   
        self.remarkButton.configure(state="normal")   
        self.passButton.configure(state="normal")   
        self.exitButton.configure(state="normal") 
        self.passNextImage.configure(state="normal") 
        self.returnPrevImage.configure(state="normal") 
        
def changeButtonStateToDisabled(self):
        self.paths_button.configure(state="disabled")   
        self.saveAndSkipNextImage.configure(state="disabled")   
        self.saveAndStaySameImage.configure(state="disabled")   
        self.remarkButton.configure(state="disabled")   
        self.passButton.configure(state="disabled")   
        self.exitButton.configure(state="disabled") 
        self.passNextImage.configure(state="disabled") 
        self.returnPrevImage.configure(state="disabled") 