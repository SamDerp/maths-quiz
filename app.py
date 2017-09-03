from random import *
from operator import *

randomNumber1 = 0
randomNumber2 = 0
randomSign = 0
studentScore = 0
studentName = 0
questionNumber = 0

def startup():
    print("This is a basic Maths quiz, answer each question, at the end you will get a score.\n\n")
    while True:
        quizOrQuit = input("Do you wish to participate? (Y/N)").lower()
        if quizOrQuit not in ("yesno"):
            print("Not a valid input.")
        else:
            break
    if quizOrQuit in "yes":
        startMathsQuiz()
    else:
        quit()


def startMathsQuiz():
    questionNumber = 0
    studentName = str(input("What is your name? "))
    while True:
        try:
            maxQuestions = int(input("Enter the number of questions in integer form. "))
            break
        except:
            print("That is an invalid input. ")
            continue
    for questionNumber in range(1,maxQuestions + 1):
        askQuestion()
        print("\nYou are currently on {} / {}".format(studentScore, questionNumber))
    print("{} , your final score was {} / {}".format(studentName, studentScore, questionNumber))


def randomGenerator():
    global randomNumber1
    global randomNumber2
    global randomSign
    randomNumber1 = randint(0,10)
    randomNumber2 = randint(0,10)
    randomSign = choice(["+", "-", "*"])
    

def askQuestion():
    randomGenerator()
    global studentScore
    operator = {"+": add,
                "-": sub,
                "*": mul}
    while True:
        try:
            studentGuess = int(input("Enter the answer to {} {} {}\n".format(randomNumber1, randomSign, randomNumber2)))
            break
        except:
            print("That is an invalid answer, try again.")
            continue
    if studentGuess == operator[randomSign](randomNumber1, randomNumber2):
        print("Correct.")
        studentScore += 1
    else:
        print("Incorrect.")

startup()
