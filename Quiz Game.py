import random
import time
from collections import defaultdict



def quizGame():
    questions = defaultdict(list)
    questions = {1: ["What is the full form of CPU?", "Central Processing Unit"], 
    2: ["What is the full form of GPU?", "Graphical Processing Unit"], 
    3: ["What is the full form of RAM", "Random Access Memory"], 
    4: ["What is the full form of PSU", "Power Supply Unit"]}

    listOfQuestions = [i+1 for i in range(len(questions))]

    numberOfQuestions =  noOfQuestions(len(questions))

    # print(questions)
    # print(listOfQuestions)
    #print(numberOfQuestions) 

    listOfQuestions = random.sample(listOfQuestions, numberOfQuestions)

    # print(listOfQuestions)

    correct = 0
    incorrect = 0

    for i in listOfQuestions:
        
        print(questions[i][0])
        answer = input()

        if answer.lower() == questions[i][1].lower():
            time.sleep(1)
            print("\nYour answer is Correct!\nYou Earned 1 Point")
            correct += 1
            print("Your Current Score is " + str(correct)+"\n")
            time.sleep(1)

        else:
            incorrect += 1
            time.sleep(1)
            print("\nSorry your answer is Incorrect :( ")
            print("The correct answer is " + questions[i][1])
            print("You Earned 0 Point\nYour Current Score is " + str(correct)+".\n")

    time.sleep(1)

    print("\nYour Final Score is " + str(correct))
    print("You gave " + str(incorrect) + " incorrect out of " + str(numberOfQuestions) + " questions.")
    print("Your Percentage: " + str((correct/numberOfQuestions)*100) + "%.")

    again = input("\nWould you like to play again? Y/N \n")
    if again.lower() == "y" or again.lower() == "yes":
        print()
        quizGame()
    else:
        print("\nThank You for Playing")
        quit()




def noOfQuestions(totalQuestions):
    x = input("How many questions you want to play out of "+ str(totalQuestions) + " questions?\n")
    
    
    while True:
        if not x.isnumeric():
            x = input("\nPlease enter interger value only between 1 - " + str(totalQuestions) + ".\n")
        else:
            x = int(x)
            if x <= 0 or x > totalQuestions:
                x = input("\nPlease enter interger value only between 1 - " + str(totalQuestions) + ".\n")
            else:
                print()
                return x
    


    
print("\n ----------------  Welcome to the Quiz Game!!  ----------------\n")

time.sleep(1)

play = input("\nWould you like to play? Y/N \n")

if play.lower() == "yes" or play.lower() == "y":
    print()
    time.sleep(0.2)
    pass
else:
    print("Thank You for Visiting :)")
    quit()

quizGame()

