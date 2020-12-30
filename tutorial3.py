from tkinter import*

root = Tk()

judul1 = Label(root, text="judul program 1", bg = "red", fg = "white")
judul1.pack()

judul2 = Label(root, text="judul program 2", bg = "blue", fg = "white")
judul2.pack(fill=X)

judul3 = Label(root, text="judul program 3", bg = "black", fg = "white")
judul3.pack(side=RIGHT, fill=Y)
root.mainloop()