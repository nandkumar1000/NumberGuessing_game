import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    user_input = entry.get()
    try:
        user_input = int(user_input)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    if user_input > computer_number:
        messagebox.showinfo("Result", "Your guess is too high!")
    elif user_input < computer_number:
        messagebox.showinfo("Result", "Your guess is too low!")
    else:
        messagebox.showinfo("Result", "Congratulations! You guessed the number!")
        restart_game()

def restart_game():
    global computer_number
    computer_number = random.randint(1, 1200)
    entry.delete(0, tk.END)

# Initialize Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

# Generate random number
computer_number = random.randint(1, 1200)

# Create widgets
label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
