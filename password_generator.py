# Importing Required Libraries
from tkinter import *
import tkinter
import random


# Creating GUI Window: Title, Geometry, Label
win = Tk()
win.title("CLARSEN: Password Generator_Python")
win.geometry("500x300")
Label(win, font=("Bookman Old Style", 12),
      text="GENERATE YOUR PASSWORD", fg="blue").pack()


# Creating Password_Generator() Function
def password_generate(leng):
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.!&*+_^%$#"
    password = " ".join(random.sample(valid_char, leng))
    p = Label(win, text=password, font=(
        "Arial Rounded MT Bold", 20), fg="green").place(x=110, y=230)


# #converting string input to integer
check1 = tkinter.IntVar()
check2 = tkinter.IntVar()
check3 = tkinter.IntVar()
check4 = tkinter.IntVar()


# Creating CheckBoxes
Checkbutton(win, font="bold", text="4 character",
            onvalue=4, variable=check1).pack()
Checkbutton(win, font="bold", text="6 character",
            onvalue=6, variable=check2).pack()
Checkbutton(win, font="bold", text="8 character",
            onvalue=8, variable=check3).pack()
Checkbutton(win, font="bold", text="12 character",
            onvalue=12, variable=check4).pack()


# Creating message() Function
def message():
    m = Label(win, text="Please, choose your password length above!", font=(
        "Arial Rounded MT Bold", 15), fg="red").place(x=25, y=200)


# Function to get the length of Password
def get_var():
    if check1.get() == 4:
        password_generate(4)
    elif check2.get() == 6:
        password_generate(6)
    elif check3.get() == 8:
        password_generate(8)
    elif check4.get() == 12:
        password_generate(12)
    else:
        message()


# Creating Button and Main Command to Run
Button(win, text="Generate", font=("bold", 10),
       bg="Yellow", command=get_var).pack()

win.mainloop()
