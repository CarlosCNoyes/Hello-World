import tkinter as tk
import random
import time

# Main game class
class WhackAMole:

    def __init__(self, master):
        self.master = master
        self.master.title("Whack a Mole!")

        self.score = 0
        self.moles = []
        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack()

        self.draw_grid()
        self.draw_score()

        self.master.after(1000, self.add_mole)

    def draw_grid(self):
        # Create a 3x3 grid of buttons
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.game_frame, text="    ", state=tk.DISABLED)
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.moles.append(row)

    def draw_score(self):
        # Display the current score
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack()

    def add_mole(self):
        # Add a mole to a random position
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        # Configure the button at this position
        self.moles[row][col].config(text="Mole", state=tk.NORMAL, command=lambda: self.hit_mole(row, col))

        # Remove the mole after 1 second
        self.master.after(1000, lambda: self.remove_mole(row, col))

        # Add a new mole every second
        self.master.after(1000, self.add_mole)

    def remove_mole(self, row, col):
        # Remove a mole from the specified position
        self.moles[row][col].config(text="    ", state=tk.DISABLED)

    def hit_mole(self, row, col):
        # Process a mole hit
        if self.moles[row][col]['text'] == "Mole":
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.remove_mole(row, col)

# Create the main application window
root = tk.Tk()
game = WhackAMole(root)
root.mainloop()
