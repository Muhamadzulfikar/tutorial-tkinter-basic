# membuat massage box

from tkinter import*
import tkinter.messagebox

root = Tk()

jawab = tkinter.messagebox.askquestion('keluar', 'apakah anda ingin keluar ?')

tombol1 = Button(root, text="exit")
tombol1.pack(side=LEFT)

if jawab == "yes":
    exit()

root.mainloop()