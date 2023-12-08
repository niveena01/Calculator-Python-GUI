from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('calculator')
root.geometry('300x380')

input_value = StringVar()
expression = ""

def button_click(num):
    global expression
    expression = expression + num
    input_value.set(expression)

def button_equal():
    global expression
    result = str(eval(expression))
    input_value.set(result)
    expression = ""

def button_clr():
    global expression
    expression = ""
    input_value.set(expression)


entry_box = Label(root, textvariable=input_value, width=20, font='bold', height=2, background='light grey')
entry_box.place(x=50, y=20)

Button(root, text='7', font='bold', width=3, command=lambda: button_click('7')).place(x=50, y=80)
Button(root, text='8', font='bold', width=3, command=lambda: button_click('8')).place(x=100, y=80)
Button(root, text='9', font='bold', width=3, command=lambda: button_click('9')).place(x=150, y=80)
Button(root, text='x', font='bold', width=3, command=lambda: button_click('*')).place(x=200, y=80)

Button(root, text='4', font='bold', width=3, command=lambda: button_click('4')).place(x=50, y=130)
Button(root, text='5', font='bold', width=3, command=lambda: button_click('5')).place(x=100, y=130)
Button(root, text='6', font='bold', width=3, command=lambda: button_click('6')).place(x=150, y=130)
Button(root, text='-', font='bold', width=3, command=lambda: button_click('-')).place(x=200, y=130)

Button(root, text='1', font='bold', width=3, command=lambda: button_click('1')).place(x=50, y=180)
Button(root, text='2', font='bold', width=3, command=lambda: button_click('2')).place(x=100, y=180)
Button(root, text='3', font='bold', width=3, command=lambda: button_click('3')).place(x=150, y=180)
Button(root, text='+', font='bold', width=3, command=lambda: button_click('+')).place(x=200, y=180)

Button(root, text='0', font='bold', width=3, command=lambda: button_click('0')).place(x=50, y=230)
Button(root, text='.', font='bold', width=3, command=lambda: button_click('.')).place(x=100, y=230)
Button(root, text='/', font='bold', width=3, command=lambda: button_click('/')).place(x=150, y=230)
Button(root, text='=', font='bold', width=3, command=lambda: button_equal()).place(x=200, y=230)

Button(root, text='clear', font='bold', width=20, command=lambda: button_clr()).place(x=50, y=280)

root.mainloop()
