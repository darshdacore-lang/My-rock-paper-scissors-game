import random


class Scoreboard:
    def __init__(self):
        self.player = 0
        self.computer = 0

    def add_point(self, winner):
        if winner == "player":
            self.player += 1
        elif winner == "computer":
            self.computer += 1

    def has_winner(self, target_score):
        return self.player >= target_score or self.computer >= target_score

    def display(self):
        print(f"Score -> You: {self.player} | Computer: {self.computer}")


class RockPaperScissorsGame:
    choices = ("rock", "paper", "scissors")
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    def __init__(self, target_score=3):
        self.target_score = target_score
        self.scoreboard = Scoreboard()
        self.round_number = 0

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        self.round_number += 1

        if player_choice == computer_choice:
            result = "tie"
        elif self.beats[player_choice] == computer_choice:
            result = "player"
        else:
            result = "computer"

        self.scoreboard.add_point(result)
        return computer_choice, result

    def is_over(self):
        return self.scoreboard.has_winner(self.target_score)


class ConsoleUI:
    def get_player_choice(self, choices):
        while True:
            choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
            if choice in choices:
                return choice
            print("Invalid choice. Please choose rock, paper, or scissors.")

    def play_match(self):
        game = RockPaperScissorsGame()
        print(f"\nStarting a new match! First to {game.target_score} wins.")

        while not game.is_over():
            player_choice = self.get_player_choice(game.choices)
            computer_choice, result = game.play_round(player_choice)

            print(f"Computer chose: {computer_choice}")
            print(f"You chose: {player_choice}")
            print({"tie": "It's a tie!", "player": "You win this round!", "computer": "Computer wins this round!"}[result])
            game.scoreboard.display()

        winner = "You" if game.scoreboard.player > game.scoreboard.computer else "Computer"
        print(f"\n{winner} won the match!")
        input("Press Enter to return to the menu.")

    def run(self):
        while True:
            print("\n=== ROCK PAPER SCISSORS ===")
            print("1. Play Game\n2. How to Play\n3. Quit")
            choice = input("Choose an option (1-3): ").strip()

            if choice == "1":
                self.play_match()
            elif choice == "2":
                print("\nRock beats scissors, paper beats rock, and scissors beats paper.")
                input("Press Enter to return to the menu.")
            elif choice == "3":
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    ConsoleUI().run()
