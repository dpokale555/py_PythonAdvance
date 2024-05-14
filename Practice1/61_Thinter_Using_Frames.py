from tkinter import *

root =Tk()

Frame1= Frame(root)
Frame1.pack()

Frame2= Frame(root)
Frame2.pack(side=BOTTOM)

button1= Button(Frame1, text="Click Here", fg="Red")
button2= Button(Frame2, text="Click Here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()


