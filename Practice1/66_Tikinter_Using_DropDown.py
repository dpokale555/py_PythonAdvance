from tkinter import *

def function1():
    print("This is menu item clicked")


root=Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu1 = Menu(mymenu)
submenu2 = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu1)
mymenu.add_cascade(label="View", menu=submenu2)

submenu1.add_command(label="Project", command=function1)
submenu1.add_command(label="Save", command=function1)
submenu1.add_separator()
submenu1.add_command(label="Exit", command=function1)
submenu1.add_command(label="Undo", command=function1)

submenu2.add_command(label="Layout", command=function1)
submenu2.add_command(label="PrintView", command=function1)
submenu2.add_separator()
submenu2.add_command(label="Remark", command=function1)


root.mainloop()