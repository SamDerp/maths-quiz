from random import randint, choice
from operator import add, mul, sub
from uuid import uuid4
from tkinter import *
from tkinter import ttk
from Classes.Mongo import Mongo


class MathsQuiz(object):
    
    def __init__(self):
        self.root = Tk() 
        self.studentName = 0
        self.studentInput = IntVar()
        self.mathsQuestion = StringVar()
        self.operator = {"+": add,
                         "-": sub,
                         "*": mul}
        self.randomNumber1 = 0
        self.randomNumber2 = 0
        self.randomSign = 0
        self.studentScore = 0
        self.uniqueID = 0
        self.questionNumber = 0
        self.maxQuestion = 0
        self.maxAddition = 0
        self.maxSubtraction = 0
        self.maxMultiplication = 0
        self.start_quiz()

    def store_to_database(self):
        while True:
            while True:
                haveUID = input("Do you have a UID? It will be in the format: \nxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\n(Y/N): ").lower()
                if haveUID not in "yes":
                    if haveUID not in "no":
                        print("Invalid input, please try again.")
                    else:
                        break
                else:
                    break
            if haveUID != "" and haveUID  in "yes":
                self.uniqueID = input("Please input your UID correctly with no spaces. ")
                studentRecord = Mongo(self.uniqueID, self.studentName, self.studentScore)
                studentRecord.overwrite_score_from_database()
                break
            elif haveUID != "" and haveUID  in "no":
                self.uniqueID = str(uuid4())
                print(self.uniqueID,"\nThis is your UID. You will need it to log back into your account. So write it down.")
                studentRecord = Mongo(self.uniqueID, self.studentName, self.studentScore)
                studentRecord.store_to_database()
                break
            else:
                print("Invalid input, please try again.")

    def start_quiz(self):
        self.studentName = str(input("What is your name? "))
        while True:
            try:
                self.maxQuestions = int(input("Enter the number of questions in integer form. "))
                break
            except:
                print("That is an invalid input. ")
                continue
        while True:
            try:
                self.maxAddition = int(input("Enter the maximum score for addition questions. "))
                break
            except:
                print("That is an invalid input. ")
                continue
        while True:
            try:
                self.maxSubtraction = int(input("Enter the maximum score for subtraction questions. "))
                break
            except:
                print("That is an invalid input. ")
                continue
        while True:
            try:
                self.maxMultiplication = int(input("Enter the maximum score for multiplication questions. "))
                break
            except:
                print("That is an invalid input. ")
                continue
        self.generate_calculator()
        self.question_checker()
        
    def question_checker(self):
        if self.questionNumber == self.maxQuestions - 1:
            try:
                self.root.destroy()
                print("{} , your final score was {}".format(self.studentName,self.studentScore))
                self.store_to_database()
            except:
                pass
        else:
            self.symbol_checker()
            self.ask_question()
            self.questionNumber = self.questionNumber + 1
            print("\nYou are currently on {} points.".format(self.studentScore))

    def symbol_checker(self):
        if self.maxMultiplication >= self.studentScore >= self.maxSubtraction:
            self.symbol = "*"
        elif self.maxSubtraction >= self.studentScore >= self.maxAddition:
            self.symbol = "-"
        else:
            if self.studentScore <= self.maxAddition:
                self.symbol = "+"

    def ask_question(self):
        self.random_generator()
        self.symbol_checker()
        self.question = "Enter the answer to {} {} {}\n".format(self.randomNumber1, self.symbol, self.randomNumber2)
        self.mathsQuestion.set(self.question)

    def random_generator(self):
        self.randomNumber1 = randint(0, 10)
        self.randomNumber2 = randint(0, 10)

    def check_math(self):
        print(self.studentInput.get())
        if self.studentInput.get() == self.operator[self.symbol](self.randomNumber1, self.randomNumber2):
            print("Correct.")
            self.studentScore += 1
        else:
            print("Incorrect.")
            self.studentScore -= 1
        self.studentInput.set(0)
        self.question_checker()

    def generate_calculator(self):
        self.root.title("Maths Quiz")
        correct = StringVar()
        self.ask_question()
        mathsQuestionLabel = Label(self.root, textvariable=self.mathsQuestion, height=2, width=20)
        mathsQuestionLabel.grid(row=1, column=0, sticky=N)
        studentInputLabel = Label(self.root, textvariable=self.studentInput, height=2, width=20)
        studentInputLabel.grid(row=2, column=0, sticky=N)
        Grid.rowconfigure(self.root, 0, weight=1) 
        Grid.columnconfigure(self.root, 0, weight=1)
        frame=Frame(self.root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)
        rowIndex = 0 
        buttonText = 1 
        while rowIndex != 4:
            Grid.rowconfigure(frame, rowIndex, weight=1) 
            rowIndex = rowIndex + 1
            colIndex = 0 
            while colIndex != 3: 
                Grid.columnconfigure(frame, colIndex, weight=1) 
                btn = ttk.Button(frame) 
                btn.grid(row=rowIndex, column=colIndex, sticky=N+S+E+W) 
                colIndex = colIndex + 1 
                btn['text'] =buttonText
                btn['command'] =lambda x=buttonText: self.studentInput.set(self.studentInput.get()*10 + x)
                buttonText = buttonText + 1
                if buttonText ==11: 
                    btn['text'] ="-"
                    btn['command'] =lambda : self.studentInput.set(-self.studentInput.get())
                if buttonText ==12: 
                    btn['text'] ="⌫"
                    btn['command'] =lambda : self.studentInput.set(0)
                if buttonText == 13:
                    btn['text'] ="↵"
                    btn['command'] =lambda : self.check_math()
                btn = ttk.Button(frame) 
                btn.grid(row=5, column=1, sticky=N+S+E+W) 
                btn['text'] ="0"
                btn['command'] =lambda : self.studentInput.set(self.studentInput.get()*10)
        self.root.mainloop()


