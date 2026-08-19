import random

print("Welcome to the rock paper scissors game")

num_rounds = int(input("Select the number of rounds you want to play: "))

player_score = 0
computer_score = 0

#loop through each round

for round in range(num_rounds):
    print(f"\nRound {round + 1}")
    player_choice = input("Enter your choice, rock, paper or scissors:").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    print(f"Round {round + 1} result:")

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