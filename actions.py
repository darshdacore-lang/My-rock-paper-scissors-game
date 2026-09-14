import random

def get_action():
    actions = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(actions)

action = get_action()

if action == "rock":
    print("you chose rock")
elif action == "paper":
    print("you chose paper")
elif action == "scissors":
    print("you chose scissors")
elif action == "lizard":
    print("you chose lizard")
elif action == "spock":
    print("you chose spock")

choices = ["rock", "paper", "scissors", "lizard", "spock"]
player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower().strip()

while player_choice not in choices:
    print("Invalid choice. Please choose rock, paper, scissors, lizard, or spock.")
    player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower().strip()

