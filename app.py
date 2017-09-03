from random import *
from operator import *

studentUsers = {}

class MathsQuiz(object):
    def __init__(self, studentName):
        self.studentName = studentName
        self.randomNumber1 = 0
        self.randomNumber2 = 0
        self.randomSign = 0
        self.studentScore = 0

    def startQuiz(self):
        questionNumber = 0
        while True:
            try:
                maxQuestions = int(input("Enter the number of questions in integer form. "))
                break
            except:
                print("That is an invalid input. ")
                continue
        for questionNumber in range(1,maxQuestions + 1):
            self.askQuestion()
            print("\nYou are currently on {} / {}".format(self.studentScore, questionNumber))
        print("{} , your final score was {} / {}".format(self.studentName, self.studentScore, questionNumber))

    def randomGenerator(self):
        self.randomNumber1 = randint(0,10)
        self.randomNumber2 = randint(0,10)
        self.randomSign = choice(["+", "-", "*"])

    def askQuestion(self):
        self.randomGenerator()
        operator = {"+": add,
                    "-": sub,
                    "*": mul}
        while True:
            try:
                studentGuess = int(input("Enter the answer to {} {} {}\n".format(self.randomNumber1, self.randomSign, self.randomNumber2)))
                break
            except:
                print("That is an invalid answer, try again.")
                continue
        if studentGuess == operator[self.randomSign](self.randomNumber1, self.randomNumber2):
            print("Correct.")
            self.studentScore += 1
        else:
            print("Incorrect.")


def startup():
    print("This is a basic Maths quiz, answer each question, at the end you will get a score.\n\n")
    while True:
        quizOrQuit = input("Do you wish to participate? (Y/N)").lower()
        if quizOrQuit not in ("yesno"):
            print("Not a valid input.")
        else:
            break
    if quizOrQuit in "yes":
        studentName = str(input("What is your name? "))
        studentUsers[studentName] = MathsQuiz(studentName)
        studentUsers[studentName].startQuiz()
    else:
        quit()

startup()
