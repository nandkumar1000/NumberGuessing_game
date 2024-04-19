import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("300x200")
        
        self.computer_number = random.randint(1, 1200)
        
        self.label = tk.Label(self, text="Enter a number:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)
        
        self.guess_button = tk.Button(self, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)
        
    def check_guess(self):
        user_input = self.entry.get()
        try:
            user_input = int(user_input)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
        
        if user_input > self.computer_number:
            messagebox.showinfo("Result", "Your guess is too high!")
        elif user_input < self.computer_number:
            messagebox.showinfo("Result", "Your guess is too low!")
        else:
            messagebox.showinfo("Result", "Congratulations! You guessed the number!")
            self.restart_game()
    
    def restart_game(self):
        self.computer_number = random.randint(1, 1200)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()
