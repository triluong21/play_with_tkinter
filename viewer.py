from ast import Lambda
from re import L
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Work with Images")
root.iconbitmap('pictures/mask_icon.ico')


my_img1 = ImageTk.PhotoImage(Image.open("pictures/Aquaman.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("pictures/farmhouse.png"))

image_list = [my_img1, my_img2]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=2, relief=SUNKEN, anchor=W)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[img_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(img_number - 1))
    
    if img_number == 2:
        button_forward = Button(root, text=">>", state=DISABLED)



    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)       
    status = Label(root, text="Image " + str(img_number) + " of " + str(len(image_list)), bd=2, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(img_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[img_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(img_number - 1))
    
    if img_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)   
    status = Label(root, text="Image " + str(img_number) + " of " + str(len(image_list)), bd=2, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=20)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
