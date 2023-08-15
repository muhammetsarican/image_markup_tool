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