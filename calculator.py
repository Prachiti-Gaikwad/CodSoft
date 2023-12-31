import tkinter as tk

def press(num):
    expression = equation.get()
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        expression = equation.get()
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("Error")

def clear():
    equation.set("")

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Simple Calculator")
    gui.geometry("350x175")
    gui.resizable(False, False) 

    equation = tk.StringVar()

    expression_field = tk.Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

 
    buttons = [
        ["1", "2", "3", "+"],
        ["4", "5", "6", "-"],
        ["7", "8", "9", "*"],
        ["0", ".", "=", "/"]
    ]

    for row, button_row in enumerate(buttons):
        for col, button_text in enumerate(button_row):
            button = tk.Button(gui, text=button_text, fg='black', bg='grey', height=1, width=11)
            button.grid(row=row+2, column=col)

            if button_text.isdigit() or button_text == ".":
                button.config(command=lambda num=button_text: press(num))
            elif button_text == "=":
                button.config(command=equalpress)
            else:
                button.config(command=lambda op=button_text: press(op))

    clear_button = tk.Button(gui, text="Clear", fg='black', bg='grey', height=1, width=11, command=clear)
    clear_button.grid(row=5, column=1)

    gui.mainloop()