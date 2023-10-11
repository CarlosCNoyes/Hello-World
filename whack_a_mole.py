import tkinter as tk
import random
import time
from tkinter import messagebox

class WhackAMole:

    def __init__(self, master):
        self.master = master
        self.master.title("Whack a Mole!")

        self.score = 0
        self.game_time = 30  # game duration in seconds
        self.end_time = time.time() + self.game_time  # when the game will end
        self.moles = []
        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack()

        self.draw_grid()
        self.draw_score()
        self.draw_timer()

        self.update_timer()
        self.master.after(1000, self.add_mole)

    def draw_grid(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.game_frame, text="    ", state=tk.DISABLED)
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.moles.append(row)

    def draw_score(self):
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack()

    def draw_timer(self):
        self.timer_label = tk.Label(self.master, text=f"Time left: {self.game_time}")
        self.timer_label.pack()

    def update_timer(self):
        # Calculate the remaining time and update the timer label
        remaining_time = int(self.end_time - time.time())
        self.timer_label.config(text=f"Time left: {max(remaining_time, 0)}")

        if remaining_time <= 0:
            self.end_game()
        else:
            # Update the timer every second
            self.master.after(1000, self.update_timer)

    def add_mole(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        self.moles[row][col].config(text="Mole", state=tk.NORMAL, command=lambda: self.hit_mole(row, col))
        self.master.after(1000, lambda: self.remove_mole(row, col))

        # Continue the game if there is still time left
        if time.time() < self.end_time:
            self.master.after(1000, self.add_mole)

    def remove_mole(self, row, col):
        self.moles[row][col].config(text="    ", state=tk.DISABLED)

    def hit_mole(self, row, col):
        if self.moles[row][col]['text'] == "Mole":
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.remove_mole(row, col)

    def end_game(self):
        # End the game by disabling all buttons and showing a final message
        for row in self.moles:
            for button in row:
                button.config(text="    ", state=tk.DISABLED)
        tk.messagebox.showinfo("Time's up!", f"Game over! Your final score is {self.score}")

# Create the main application window
root = tk.Tk()
game = WhackAMole(root)
root.mainloop()
