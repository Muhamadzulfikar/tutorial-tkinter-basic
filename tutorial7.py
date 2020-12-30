from tkinter import*


def dropdown() :
    print("menu klik 1")


root = Tk()

menu = Menu(root)
root.config(menu = menu)
submenu = Menu(menu)
menu.add_cascade(label = "file", menu = submenu)
submenu.add_command(label = "new project", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "new ", command = dropdown)
submenu.add_command(label = "Save as", command = dropdown)

editmenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut", command = dropdown)

viewmenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = viewmenu)

root.mainloop()