# membuat toolbar

from tkinter import*

def dropdown():
    print("hasil klik")

root = Tk()

toolbar = Frame(root, bg="red")

tombol1 = Button(toolbar, text="insert", command = dropdown)
tombol1.pack(side=LEFT, padx = 3, pady = 3)

tombol2 = Button(toolbar, text="print", command = dropdown)
tombol2.pack(side=LEFT, padx = 3, pady = 3)

toolbar.pack(side=TOP, fill=X)
root.mainloop()