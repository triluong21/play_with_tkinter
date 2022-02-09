from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title("Using Frame")
root.iconbitmap("pictures/mask_icon.ico")

frame = LabelFrame(root, text="This is my frame", padx=95, pady=95)
frame.grid(row=0, column=0)

b = Button(frame, text="Click Me")
b.pack()



root.mainloop()
