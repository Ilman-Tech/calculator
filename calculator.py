import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title('Calculator')  # Set the title of the window
root.geometry('300x420')  # Set the dimensions of the window
root.resizable(False, False)  # Prevent resizing of the window

# Create an entry widget for displaying and entering numbers and expressions
entry = tk.Entry(root, font=("Arial", 14), bd=5, relief=tk.SUNKEN, justify="right")
entry.grid(column=0, row=0, columnspan=4, padx=5, pady=5)

# Define the calculator buttons and their positions in the grid
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
]

# Function to calculate the entered expression
def calculate():
    try:
        # Evaluate the entered expression and display the result
        global result
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        # Show an error message if the input is invalid
        messagebox.showerror("Error", "Invalid input")

# Function to append a value to the entry field
def append_value(value):
    entry.insert(tk.END, value)

# Function to clear the entire entry field
def clear_btn():
    entry.delete(0, tk.END)

# Function to delete the last character from the entry field
def backspcae():
    currter_text = entry.get()
    if currter_text:
        entry.delete(len(currter_text) - 1, tk.END)

# Create the "Clear" button to clear the entry field
clear = tk.Button(root, text="C", command=clear_btn, font=("Arial", 14), width=10, height=2)
clear.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

# Create the "Backspace" button to remove the last character
back = tk.Button(root, text="◀", font=("Arial", 14), command=backspcae, width=10, height=2)
back.grid(column=2, row=1, columnspan=2, padx=5, pady=5)

# Function to create number and operator buttons
def create_btn(text, row, col):
    if text == '=':
        # Button for calculating the result
        btn = tk.Button(root, text=text, command=calculate, font=("Arial", 14), width=5, height=2)
    else:
        # Other buttons to append values to the entry field
        btn = tk.Button(root, text=text, command=lambda: append_value(text), font=("Arial", 14), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5, columnspan=1)

# Create buttons based on the "buttons" list
for (text, row, col) in buttons:
    create_btn(text, row, col)

# Start the main event loop
root.mainloop()
