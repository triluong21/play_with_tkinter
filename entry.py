from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=2, bg="blue", fg="red")
e.pack()
e.insert(0, "Enter your name...")

def myClick():
    myLabel3 = Label(root, text="Hi " + e.get())
    myLabel3.pack()

myButton = Button(root, text="Enter Your Name", command=myClick, bg='yellow', fg='blue')
myButton.pack()

root.mainloop()