def display_scoreboard(score_player, score_computer):
    print("\n=== SCOREBOARD ===")
    print(f"You: {score_player} | Computer: {score_computer}")

    if score_player > score_computer:
        print("You win the match!")
    elif score_player < score_computer:
        print("Computer wins the match!")
    else:
        print("The match is a tie!")

