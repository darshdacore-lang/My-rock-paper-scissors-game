import random

print("Welcome to the rock paper scissors game")

num_rounds = int(input("Select the number of rounds you want to play: "))

player_score = 0
computer_score = 0

# Loop through each round
for round_num in range(1, num_rounds + 1):
    print(f"\n--- Round {round_num} ---")
    
    # Get player choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Get computer choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print(f"Score: You {player_score} - Computer {computer_score}")

# Show final results
print(f"\nFinal Score: You {player_score} - Computer {computer_score}")