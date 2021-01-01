# membuat line dan shape


from tkinter import*

root = Tk()

window = Canvas(root, width=300, height=200)
window.pack()

hitam = window.create_line(0,0,200,50)
merah = window.create_line(0,150,300,50, fill = "red")
oval_biru = window.create_oval(20, 70, 110, 160, fill = "blue")


kotak_hijau =  window.create_rectangle(30, 50, 100, 150, fill = "green")
root.mainloop()