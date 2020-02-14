import random

plays = ["Rock", "Paper", "Scissors"]
game = True

while game:
    computer_play = random.choice(plays)
    user_play = input("Rock, Paper or Scissors?")
    if computer_play == user_play:
        print("Tie")
    elif user_play == "Rock":
        if computer_play == "Scissors":
            print("You win")
            game = False
        else:
            print("Computer wins")
            game = False
    elif user_play == "Scissors":
        if computer_play == "Rock":
            print("Computer wins")
            game = False
        else:
            print("You win")
            game = False
    elif user_play == "Paper":
        if computer_play == "Rock":
            print("You wins")
            game = False
        else:
            print("Computer wins")
            game = False
    else:
        print("Invalid play, try again")