from tkinter import *
import tkinter.messagebox


root=Tk()
tkinter.messagebox.showinfo("Popup Title", "This is the message Awesome")

response = tkinter.messagebox.askquestion("Question 1","Are you a autherise user")

if response == 'yes':
    print("Thank you for visiting")


root.mainloop()