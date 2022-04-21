import time
import random


print("\n ----------------  Welcome to the Rock Paper Scissors Game!!  ----------------\n")

time.sleep(1)

play = input("\nWould you like to play? Y/N \n")

if play.lower() == "yes" or play.lower() == "y":
    print()
    time.sleep(0.2)
    pass
else:
    print("Thank You for Visiting :)")
    quit()


def rps(): 
    numberOfRounds = noOfRounds()

    count = 1

    playerWins = 0
    computerWins = 0
    draws = 0

    options = ["Rock", "Paper", "Scissors"]


    
    while count <= numberOfRounds:
        computerPlayed = random.randint(0,2)
        print("\nRound:", count)
        played = turnPlayed()

        print("You played", options[played], " and Computer played", options[computerPlayed])

        if (played == 0 and computerPlayed == 2) or (played == 1 and computerPlayed == 0) or (played == 2 and computerPlayed == 1):
            playerWins += 1
            print("You won this round!")

        elif played == computerPlayed:
            draws += 1
            print("This round was a Draw.")

        else:
            computerWins += 1
            print("Computer won this round!")

        count += 1
        print("\nYour wins:", playerWins, "Computer wins:", computerWins, "Number of Draws:", draws)

    

    if playerWins == computerWins:
        print("\nThis game was a Draw.")
    elif playerWins > computerWins:
        print("\nWoohoo!! You won this Game B)")
    else:
        print("\nYou Lose!! Better luck next time :(")

    again = input("\nWould you like to play again? Y/N \n")
    if again.lower() == "y" or again.lower() == "yes":
        print()
        rps()
    else:
        print("\nThank You for Playing")
        quit()


def noOfRounds():
    x = input("Please enter the number of rounds you want to play (Max 10 allowed): ")
    while True:
        if x.isdigit():
            x = int(x)
            if x <= 0 or x > 10:
                x = input("Please enter integer value only between 1 - 10: ")
            else:
                return x
        else:
            x = input("Please enter integer value only between 1 - 10: ")


def turnPlayed():
    print("Please enter the number corresponding to the shown option to select:\n1 : Rock\n2 : Paper\n3 : Scissors")
    x = input()
    while True:
        if x.isdigit():
            x = int(x)
            if x <= 0 or x > 3:
                x = input("Please enter integer value only between 1 - 3:\n1 : Rock\n2 : Paper\n3 : Scissors\n")
            else:
                return x-1


rps()