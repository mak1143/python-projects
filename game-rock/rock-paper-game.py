import random


def rock_paper_scissors():
    
    print(f"Welcome to Rock, Paper, Scissor! Game")
    options = ["rock","paper","scissor"]
    runing = True


    while runing:


        player = None
        computer = random.choice(options)
        #if player requess in options
        while player not in options:
            player = input("Enter a choice (rock,paper, scissors): ").lower()

        print(f"Player: {player}")
        print(f"computer: {computer}")


        if player == computer:
            print( "It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        playAgain = input("Play again? (y/n): ").lower()
        if not playAgain == "y":
            runing = False

rock_paper_scissors()
