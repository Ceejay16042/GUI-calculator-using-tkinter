
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('My first gui application(calculator)')
root.iconbitmap('C:/Users/clinton/Downloads/calc2.ico')
root.maxsize(450, 450)
# Photo = ImageTk.PhotoImage(Image.open('C:/Users/clinton/downloads/speech.png'))
# root.minsize(350, 350)
equation = StringVar()

e= Entry(width = 40, borderwidth = 5, textvariable=equation)
e.pack()
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



#define the button
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    length_of_numbers = len(e.get())
    e.delete(length_of_numbers-1, length_of_numbers)

    # equation.set("")
def button_add():
    first_number = e.get()
    global f_num
    global math
    math= "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    global s_num
    s_num = int(second_number)
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + s_num)
    if math == "subtraction":
        e.insert(0, f_num - s_num)
    if math == "multiply":
        e.insert(0, f_num * s_num)
    if math == "divide":
        e.insert(0, f_num / s_num)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


# Put the buttons on the grid
button_1 = Button(root, text="1", padx=40, activebackground="Turquoise", pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, activebackground="Turquoise", pady=20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, activebackground="Turquoise",  pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx =40, activebackground="Turquoise",  pady=20, command= lambda: button_click(0))
add_button = Button(root, text="+", padx=39, activebackground="Turquoise",  pady=20, command= lambda: button_add())
equal_button = Button(root, text="=", padx=87, activebackground="Turquoise",  pady=20, command= lambda: button_equal())
clear_button = Button(root, text="clear", padx=78, activebackground="Turquoise", pady=20, command= lambda: button_clear())
# speech_to_text_button = Button(root, image=Photo)
# speech_to_text_button.pack()


subtract_button = Button(root, text="-", padx=41, activebackground="Turquoise", pady=20, command= lambda: button_subtract())
divide_button = Button(root, text="/", padx=40, activebackground="Turquoise", pady=20, command= lambda: button_divide())
multiply_button = Button(root, text="*", padx=41, activebackground="Turquoise", pady=20, command= lambda: button_multiply())
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
add_button.grid(row=5, column=0)
clear_button.grid(row=4, column=1, columnspan=2)
equal_button.grid(row=5, column=1, columnspan=2)

subtract_button.grid(row=6, column=0)
multiply_button.grid(row=6, column=1)
divide_button.grid(row=6, column=2)
##
root.mainloop()
