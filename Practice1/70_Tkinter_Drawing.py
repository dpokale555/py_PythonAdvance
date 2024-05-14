from tkinter import *

root=Tk()
canvas1 = Canvas(root, width=20000, height=10000)
canvas1.pack()

newline1 = canvas1.create_line(0,0, 10000, 10000)
newline2 = canvas1.create_line(10,10, 20000, 10000, fill="green")


root.mainloop()