import random
import tkinter as tk


CHOICES = ["Rock", "Paper", "Scissors"]

BEATS = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}


class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0

        tk.Label(
            root,
            text="Rock Paper Scissors",
            font=("Arial", 26, "bold"),
        ).pack(pady=25)

        self.score_label = tk.Label(
            root,
            text="You: 0    Computer: 0",
            font=("Arial", 18),
        )
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(
            root,
            text="Choose your move!",
            font=("Arial", 16),
            justify="center",
        )
        self.result_label.pack(pady=25)

        button_frame = tk.Frame(root)
        button_frame.pack()

        for choice in CHOICES:
            tk.Button(
                button_frame,
                text=choice,
                font=("Arial", 14),
                width=10,
                command=lambda move=choice: self.play_round(move),
            ).pack(side="left", padx=5)

        tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 12),
            command=self.reset_game,
        ).pack(pady=30)

    def play_round(self, player_choice):
        computer_choice = random.choice(CHOICES)

        if player_choice == computer_choice:
            result = "Draw!"
        elif BEATS[player_choice] == computer_choice:
            self.player_score += 1
            result = "You win this round!"
        else:
            self.computer_score += 1
            result = "Computer wins this round!"

        self.score_label.config(
            text=f"You: {self.player_score}    "
            f"Computer: {self.computer_score}"
        )

        self.result_label.config(
            text=(
                f"You chose: {player_choice}\n"
                f"Computer chose: {computer_choice}\n\n"
                f"{result}"
            )
        )

        if self.player_score == 3 or self.computer_score == 3:
            winner = (
                "You won the match!"
                if self.player_score == 3
                else "Computer won the match!"
            )
            self.result_label.config(text=f"{winner}\nClick Reset Game to play again.")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0

        self.score_label.config(text="You: 0    Computer: 0")
        self.result_label.config(text="Choose your move!")


root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()