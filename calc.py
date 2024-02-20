import tkinter as tk
from math import *

def onButtonClick(text):
    global expression
    if text == '=': 
        try:
            resultsVar.set(eval(expression)) # eval runs the expression as python code
        except Exception as e: # catch erros and set them to the var e
            resultsVar.set("Error")
            print(e)
            expression = ""
    elif text == 'del':
        expression = expression[:-1] # remove last element in the string
        resultsVar.set(expression)
    elif text == 'clr':
        expression = ""
        resultsVar.set("")
    elif text == 'pi':
        expression += 3.141
        resultsVar.set(expression)
    elif text == 'x!':
        expression = f'factorial({expression})' # wrap whole expression in the factorial function
        resultsVar.set(expression)
    elif text == 'e^x':
        expression = f'exp({expression})'
        resultsVar.set(expression)
    elif text == 'ln':
        expression = f'log({expression})'
        resultsVar.set(expression)
    elif text == 'x^y':
        expression += '**'
        resultsVar.set(expression)
    elif text == 'sqrt':
        expression = f'sqrt({expression})'
        resultsVar.set(expression)
    elif text == '10^x':
        expression = f'10**({expression})'
        resultsVar.set(expression)
    elif text == 'log':
        expression = f'log10({expression})'
        resultsVar.set(expression)
    else:
        expression += text # for in general, like handling numbers and also the trig functions, where you need to use ( and )
        resultsVar.set(expression)

root = tk.Tk()
root.title("calculator for cool people")

expression = ""
resultsVar = tk.StringVar()

entryFrame = tk.Frame(root)
entryFrame.pack(
    side=tk.TOP, 
    padx=10, 
    pady=10
)

entry = tk.Entry(
    entryFrame, 
    textvariable=resultsVar, 
    font=('Arial', 18), 
    bd=5, 
    insertwidth=4, 
    width=15, 
    justify='right'
)

entry.grid(
    row=0, 
    column=0, 
    padx=0, 
    pady=0, 
    columnspan=7
)

buttonFrame = tk.Frame(
    root
)
buttonFrame.pack(
    side=tk.TOP
)

buttons = [ # we create the buttons here
    ['acos', 'asin', 'atan', 'del', 'clr'],
    ['cos', 'sin', 'tan', 'e^x', 'ln'],
    ['x^y', 'sqrt', '10^x', 'log', '('],
    ['7', '8', '9', 'x!', ')'],
    ['4', '5', '6', '*', '/'],
    ['1', '2', '3', '+', '-'],
    ['0', '.', '+/-', 'pi', '='],
]

for i, row in enumerate(buttons): # enumerate over buttons, not needed but more readble than doing buttons[i]
    for j, text in enumerate(row):
        button = tk.Button(
            buttonFrame, 
            text=text, 
            font=('Arial', 12), 
            bd=5, 
            padx=10, 
            pady=10, 
            command=lambda t=text: onButtonClick(t) # lambda function to run always when called
        )
        button.grid(
            row=i+1, 
            column=j, 
            padx=2, 
            pady=2
        )



root.mainloop()
