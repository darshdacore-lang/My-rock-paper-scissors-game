def check_win_loss(player_score, computer_score):
    if player_score > computer_score:
        print("You win the match!")
    elif computer_score > player_score:
        print("Computer wins the match!")
    else:
        print("The match is a draw!")

        check_win_loss(3,2)