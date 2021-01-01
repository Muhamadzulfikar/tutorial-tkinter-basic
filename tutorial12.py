# input image

from tkinter import*

root = Tk()

photo = PhotoImage(file = "map.jpg")
label = label(root, image = photo)
label.pack()

root.mainloop()