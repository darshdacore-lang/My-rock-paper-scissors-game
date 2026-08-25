import random

choices = ["rock", "paper", "scissors"]

print("Five round mode")

for round_number in range(1, 6):
    print(f"\nRound {round_number}")

    player_choice = input("Enter your choice, rock, paper or scissors: ").lower().strip()
    while player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Enter your choice, rock, paper or scissors: ").lower().strip()

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    print("Round result:")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
    else:
        print("You lose this round!")

        