from tkinter import*

root = Tk()

ceklist1 = Checkbutton(root, text="ceklist1")
ceklist2 = Checkbutton(root, text="ceklist2")
ceklist3 = Checkbutton(root, text="ceklist3")

ceklist1.grid(columnspan=2)
ceklist2.grid(columnspan=2)
ceklist3.grid(row=1,column=2)

root.mainloop()