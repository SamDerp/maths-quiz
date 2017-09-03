from random import * #This method is prefered over 'import random' as it means 'random' prefix isn't required
def startup():
    print("This is a basic Maths quiz, there will be 10 questions, answer each question, at the end you will get a score out of 10.\n\n")
    quizOrQuit = input("Do you wish to participate? (Y/N)")
    if quizOrQuit == "Y":
        mathsQuiz()
    else:
        quit()
    
    
def mathsQuiz():
    studentName = input("What is your name? ")
    studentScore = 0
    questionNumber = 1
    while questionNumber != 11:
        print("\n\nQuestion No." + str(questionNumber))
        randomNumber1 = randint(0,10)
        randomNumber2 = randint(0,10)
        randomSign = choice(["+", "-", "*"])
        print("What is " + str(randomNumber1) + " " + randomSign + " " + str(randomNumber2)+"?")#Changing randomNumber2 to a string, to make output have a questionmark at the end of the number, not a space inbetween 
        while True:
            try:
                questionGuess = int(input("Enter your answer: "))
                break
            except:
                continue
        if randomSign == "+":
            questionAnswer = randomNumber1 + randomNumber2
        elif randomSign == "-":
            questionAnswer = randomNumber1 - randomNumber2
        else:
            questionAnswer = randomNumber1 * randomNumber2
        if questionGuess == questionAnswer:
            print("Correct. ")
            studentScore += 1
        else:
            print("Incorrect. ")
        print("You are currently on " + str(studentScore) + "/" + str(questionNumber))
        questionNumber += 1
    print(studentName + ", Your final score was " + str(studentScore) + " out of 10.")
startup()
