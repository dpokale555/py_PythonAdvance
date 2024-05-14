from tkinter import *

class MyButtons:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quickbutton = Button(frame, text="Exit", command=frame.quit)
        self.quickbutton.pack(side=LEFT)

    def printmessage(self):
        print("Button clicked")


root=Tk()

b_obj= MyButtons(root)

root.mainloop()