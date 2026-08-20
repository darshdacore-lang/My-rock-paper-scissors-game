import random

print("Welcome to the rock paper scissors game")
print("First to 3 wins takes the game!")

player_score = 0
computer_score = 0
round_number = 0
choices = ["rock", "paper", "scissors"]

while player_score < 3 and computer_score < 3:
    round_number += 1
    print(f"\nRound {round_number}")

    player_choice = input("Enter your choice, rock, paper or scissors: ").lower().strip()
    while player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Enter your choice, rock, paper or scissors: ").lower().strip()

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    print("Round result:")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
if player_score == 3:
    print("Congratulations, you won the game!")
else:
    print("The computer won the game. Better luck next time!")