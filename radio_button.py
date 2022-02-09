from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title("Using Radio Button")
root.iconbitmap("pictures/mask_icon.ico")


MODES = [
    ("pepperoni", "pepperoni"),
    ("cheese", "cheese"),
    ("onion", "onion")
]

pizza = StringVar()
pizza.set("")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value).pack()

# Radiobutton(root, text="Option 1", variable=selected_option, value=1, command=lambda: clicked(selected_option.get())).pack()
# Radiobutton(root, text="Option 2", variable=selected_option, value=2, command=lambda: clicked(selected_option.get())).pack()

myLabel = Label(root, text=pizza.get()).pack()
myButton = Button(root, text="Click Me", command=lambda: clicked(pizza.get())).pack()




mainloop()
