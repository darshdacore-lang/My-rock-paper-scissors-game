import random

from scoreboard import display_scoreboard

CHOICES = ["rock", "paper", "scissors"]


def show_menu():
    print("\n=== ROCK PAPER SCISSORS ===")
    print("1. Play Game")
    print("2. How to Play")
    print("3. Quit")


def show_rules():
    print("\nHow to play:")
    print("- Rock beats scissors")
    print("- Paper beats rock")
    print("- Scissors beats paper")
    print("- First to 3 wins the match")


def get_player_choice():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
    while player_choice not in CHOICES:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
    return player_choice


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    return "computer"


def play_match():
    player_score = 0
    computer_score = 0
    round_number = 0

    print("\nStarting a new match! First to 3 wins.")

    while player_score < 3 and computer_score < 3:
        round_number += 1
        print(f"\nRound {round_number}")

        player_choice = get_player_choice()
        computer_choice = random.choice(CHOICES)

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {player_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score}")

    display_scoreboard(player_score, computer_score)

    input("\nPress Enter to return to the menu.")


def main():
    while True:
        try:
            show_menu()
            choice = input("Choose an option (1-3): ").strip()
        except EOFError:
            print("\nInput closed. Exiting the game.")
            break

        if choice == "1":
            play_match()
        elif choice == "2":
            show_rules()
            try:
                input("\nPress Enter to return to the menu.")
            except EOFError:
                print("\nReturning to the menu.")
        elif choice == "3":
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
