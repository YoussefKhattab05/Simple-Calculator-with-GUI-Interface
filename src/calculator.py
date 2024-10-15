"""
File Name: calculator.py
Description: A simple GUI calculator using Tkinter.
Author: Youssef Khattab
Email: youssefkhattab.v@gmail.com
Date Created: April 21, 2022
Last Modified: October 15, 2024
Version: 1.0

Usage:
    Run the script to open a GUI window for basic arithmetic operations.

Dependencies:
    - Tkinter (usually included with Python installations)

License:
    MIT License
"""

from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.configure(bg="#f0f0f0")
root.iconbitmap('./icon/icon.ico')
root.attributes('-alpha', 1)
root.resizable(False, False)
root.state('normal')
root.configure(cursor='cross')

e = Entry(root, width=40, background="white", foreground="black", borderwidth=5, justify="left")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    global s_num
    s_num = int(second_number)
    e.delete(0, END)
    if math == "addition":
        e.insert(0, int(f_num) + int(s_num))
    elif math == "subtraction":
        e.insert(0, int(f_num) - int(s_num))
    elif math == "multiplication":
        e.insert(0, int(f_num) * int(s_num))
    else:
        e.insert(0, int(f_num) / int(s_num))

button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=50.5, pady=25, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=50.5, pady=25, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=50.5, pady=25, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=50, pady=25, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=49, pady=25, command=button_add)
button_equal = Button(root, text="=", padx=109.5, pady=25, command=button_equal)
button_clear = Button(root, text="Clear", padx=99, pady=25, command=button_clear)

button_subtract = Button(root, text="-", padx=51, pady=25, command=button_subtract)
button_multiply = Button(root, text="*", padx=51, pady=25, command=button_multiply)
button_divide = Button(root, text="/", padx=52, pady=25, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)

root.mainloop()
