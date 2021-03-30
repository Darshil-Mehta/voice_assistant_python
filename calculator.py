from tkinter import *

root = Tk()
root.title("Calculator")


def button_click(number):
    initial = calculator_screen.get()
    calculator_screen.delete(0, END)
    calculator_screen.insert(0, str(initial) + str(number))


def btn_clear():
    calculator_screen.delete(0, END)


def btn_add():
    global operation
    global f_num
    first_number = calculator_screen.get()
    f_num = first_number
    operation = "add"
    calculator_screen.delete(0, END)


def btn_subtract():
    global operation
    global f_num
    first_number = calculator_screen.get()
    f_num = first_number
    operation = "subtract"
    calculator_screen.delete(0, END)


def btn_multiply():
    global operation
    global f_num
    first_number = calculator_screen.get()
    f_num = first_number
    operation = "multiply"
    calculator_screen.delete(0, END)


def btn_divide():
    global operation
    global f_num
    first_number = calculator_screen.get()
    f_num = first_number
    operation = "divide"
    calculator_screen.delete(0, END)


def btn_ans():
    second_number = calculator_screen.get()
    if operation == "add":
        result = int(f_num) + int(second_number)
    if operation == "subtract":
        result = int(f_num) - int(second_number)
    if operation == "multiply":
        result = int(f_num) * int(second_number)
    if operation == "divide":
        result = float(f_num) / float(second_number)
        result = int(result)
    calculator_screen.delete(0, END)
    calculator_screen.insert(0, result)


calculator_screen = Entry(root, relief=SUNKEN, bd=1)
calculator_screen.grid(row=0, column=0, columnspan=4, ipadx=150, ipady=10)

""" All buttons """
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_add = Button(root, text="+", padx=42, pady=20, command= btn_add)
button_subtract = Button(root, text="-", padx=43, pady=20, command= btn_subtract)
button_multiply = Button(root, text="*", padx=43, pady=20, command= btn_multiply)
button_divide = Button(root, text="/", padx=43, pady=20, command= btn_divide)
button_equal = Button(root, text="=", padx=40, pady=20, command= btn_ans)
button_clear = Button(root, text="clr", padx=36, pady=20, command=btn_clear)

""" Using the buttons """
button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

root.mainloop()
