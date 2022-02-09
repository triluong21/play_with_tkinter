from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Work with Images")
root.iconbitmap('pictures/mask_icon.ico')


my_img = ImageTk.PhotoImage(Image.open("pictures/Aquaman.jpeg"))
my_label = Label(image=my_img)
my_label.pack()




button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
