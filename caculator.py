import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the text entry
def update_expression(symbol):
    current_text = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, current_text + symbol)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression_entry.get())
        expression_entry.delete(0, tk.END)
        expression_entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        expression_entry.delete(0, tk.END)

# Function to clear the expression
def clear_expression():
    expression_entry.delete(0, tk.END)

# Creating main window
app = tk.Tk()
app.title("Simple Calculator")

# Entry widget for displaying the expression
expression_entry = tk.Entry(app, font=('Arial', 20), borderwidth=2, relief="solid")
expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Creating buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Placing buttons on the grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(app, text=button, font=('Arial', 20), command=evaluate_expression)
    else:
        btn = tk.Button(app, text=button, font=('Arial', 20), command=lambda b=button: update_expression(b))
    btn.grid(row=row_val, column=col_val, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_button = tk.Button(app, text='C', font=('Arial', 20), command=clear_expression)
clear_button.grid(row=row_val, column=0, columnspan=4, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")

# Adjusting column and row weights to make the buttons expand and fill space
for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Running the application
app.mainloop()
