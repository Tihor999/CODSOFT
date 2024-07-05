import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for input and result display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define button click function
def button_click(item):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(item))

# Define the function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Define the function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Create the buttons for the calculator
button_texts = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button_text in button_texts:
    action = lambda x=button_text: button_click(x) if x not in ['C', '='] else (clear() if x == 'C' else evaluate())
    button = tk.Button(root, text=button_text, width=5, height=2, font=('Arial', 18), command=action)
    button.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main event loop
root.mainloop()
