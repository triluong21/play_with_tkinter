from tkinter import *

root = Tk()

def myClick():
    myLabel3 = Label(root, text="I clicked the Button")
    myLabel3.pack()

myButton = Button(root, text="Click Me", command=myClick, fg='blue', bg='yellow')
myButton.pack()

root.mainloop()