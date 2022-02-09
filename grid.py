from cgitb import enable
from tkinter import *

root = Tk()


myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Tri").grid(row=1, column=0)

root.mainloop()