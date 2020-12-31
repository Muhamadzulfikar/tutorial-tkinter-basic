# membuat status bar

from tkinter import*

def komand():
    print("hasil klik")


root = Tk()

bingkai = Frame(root, bg="black")

tomboll1 = Button(bingkai, text="file", command=komand)
tomboll1.pack(side=LEFT, padx = 3, pady=3)

bingkai.pack(side=TOP, fill=X)

status = Label(root, text="loading .... please wait", bd = 1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()