import tkinter as tk

from menu_screen import RockPaperScissorsGame


class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.game = RockPaperScissorsGame(target_score=3)

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

        for choice in self.game.choices:
            tk.Button(
                button_frame,
            text=choice.title(),
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
        computer_choice, result = self.game.play_round(player_choice)
        result_text = {
            "tie": "It's a tie!",
            "player": "You win this round!",
            "computer": "Computer wins this round!",
        }[result]

        self.score_label.config(
            text=f"You: {self.game.scoreboard.player}    "
            f"Computer: {self.game.scoreboard.computer}"
        )

        self.result_label.config(
            text=(
                f"You chose: {player_choice}\n"
                f"Computer chose: {computer_choice}\n\n"
                f"{result_text}"
            )
        )

        if self.game.is_over():
            winner = (
                "You won the match!"
                if self.game.scoreboard.player > self.game.scoreboard.computer
                else "Computer won the match!"
            )
            self.result_label.config(text=f"{winner}\nClick Reset Game to play again.")

    def reset_game(self):
        self.game = RockPaperScissorsGame(target_score=3)

        self.score_label.config(text="You: 0    Computer: 0")
        self.result_label.config(text="Choose your move!")


root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()