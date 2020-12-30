from tkinter import*

class Buttons :  # membuat class 
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="coba klik", command=self.printMassage)
        self.printButton.pack(side = LEFT)
        
        self.quitButton = Button(frame, text="keluar", command=frame.quit)
        self.quitButton.pack(side=RIGHT)
        
    def printMassage(self):
        print("Massage ini berhasil")
            
root = Tk()

coba = Buttons(root)

root.mainloop()