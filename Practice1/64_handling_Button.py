from tkinter import *

root=Tk()

def clickbutton():
    print("You clicked the button")

button1=Button(root,text="Click Here", command=clickbutton)
button1.pack()

root.mainloop()