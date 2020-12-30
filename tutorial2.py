from tkinter import*

root = Tk()

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="tombol1", fg="red")
button2 = Button(topframe, text="tombol2", fg="blue")
button3 = Button(topframe, text="tombol3", fg="green")
button4 = Button(topframe, text="tombol4", fg="black")


button1.pack(side=TOP)
button2.pack(side=BOTTOM)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)



root.mainloop()