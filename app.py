from random import * #This method is prefered over 'import random' as it means 'random' prefix isn't required
print("This is a basic Maths quiz, there will be 10 questions, answer each question, at the end you will get a score out of 10.")
studentName = str(input("What's your name? "))
studentScore = 0
questionNumber = 1
while questionNumber != 11:
    print("\n\nQuestion No." + str(questionNumber))
    randomNumber1 = randint(0,10)
    randomNumber2 = randint(0,10)
    questionAnswer = randomNumber1 + randomNumber2
    print("What is " + str(randomNumber1) + " + " + str(randomNumber2)+"?")#Changing randomNumber2 to a string, to make output have a questionmark at the end of the number, not a space inbetween 
    questionGuess = int(input("Enter your answer: "))
    if questionGuess == questionAnswer:
        print("Correct. ")
        studentScore += 1
    else:
        print("Incorrect. ")
    print("You are currently on " + str(studentScore) + "/" + str(questionNumber))
    questionNumber += 1
print(studentName + ", Your final score was " + str(studentScore) + " out of 10.")











'''
Version 1.0 Goals
Get basic maths addition quiz working;
10 random addition questions, and return a final score out of 10.
Ask for students name
'''
