from tkinter import*


def penjumlahan(event):
    x = int(x_entry.get())
    y = int(y_entry.get())
    
    sum = x + y
    sumEntry.delete(0, "end")
    
    sumEntry.insert(0,sum)


root = Tk()

x_entry = Entry(root)
x_entry.pack(side=LEFT)

label1 = Label(root, text="+")
label1.pack(side=LEFT)

y_entry = Entry(root)
y_entry.pack(side=LEFT)

hasil = Button(root, text="=")
hasil.bind("<Button-1>", penjumlahan)
hasil.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack()


root.mainloop()