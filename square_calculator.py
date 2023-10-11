import tkinter as tk
from tkinter import messagebox

def calculate_square():
    try:
        # Try to convert the user input into a float
        user_number = float(entry.get())

        # Calculate the square
        square = user_number ** 2

        # Show the result in a message box
        messagebox.showinfo("Result", f"The square of {user_number} is {square}")
    except ValueError:
        # Error message for invalid input
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create the main application window
app = tk.Tk()
app.title("Square Calculator")

# Create a label widget
label = tk.Label(app, text="Enter a number:")
label.pack(padx=20, pady=5)

# Create an entry widget to accept user input
entry = tk.Entry(app)
entry.pack(padx=20, pady=5)

# Create a button to trigger the calculation
calculate_button = tk.Button(app, text="Calculate Square", command=calculate_square)
calculate_button.pack(padx=20, pady=20)

# Run the app
app.mainloop()
