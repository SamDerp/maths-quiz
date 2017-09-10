from random import randint, choice
from operator import add, mul, sub
from uuid import uuid4


class MathsQuiz(object):
    def __init__(self):
        self.studentName = 0
        self.randomNumber1 = 0
        self.randomNumber2 = 0
        self.randomSign = 0
        self.studentScore = 0
        self.uniqueID = 0

    def startup(self):
        self.studentName = str(input(
            "What is your name? "
        )
        )
        while True:
            # noinspection SpellCheckingInspection
            haveUID = input(
                "Do you have a UID? "
                "It will be in the format: \n"
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\n(Y/N): "
            ).lower()
            if haveUID not in "yesno":
                print(
                    "Not a valid input."
                )
            else:
                break
        if haveUID in "yes":
            self.uniqueID = input(
                "Please input your UID correctly with no spaces. "
            )
        else:
            self.uniqueID = uuid4()
            print(self.uniqueID,
                  "\nThis is your UID."
                  "You will need it to log back into your account."
                  " So write it down."
                  )
        self.start_quiz()

    def start_quiz(self):
        questionNumber = 0
        while True:

            # noinspection PyBroadException
            try:
                maxQuestions = int(input(
                    "Enter the number of questions in integer form. "
                )
                )
                break
            except:
                print(
                    "That is an invalid input. "
                )
                continue
        for questionNumber in range(1, maxQuestions + 1):
            self.ask_question()
            print(
                "\nYou are currently on {} / {}"
                .format(self.studentScore,
                        questionNumber
                        )
            )
        print(
            "{} , your final score was {} / {}"
            .format(self.studentName,
                    self.studentScore,
                    questionNumber
                    )
        )

    def random_generator(self):
        self.randomNumber1 = randint(0, 10)
        self.randomNumber2 = randint(0, 10)
        self.randomSign = choice(["+",
                                  "-",
                                  "*"])

    def ask_question(self):
        self.random_generator()
        operator = {"+": add,
                    "-": sub,
                    "*": mul}
        while True:
            # noinspection PyBroadException
            try:
                studentGuess = int(input(
                    "Enter the answer to {} {} {}\n"
                    .format(self.randomNumber1,
                            self.randomSign,
                            self.randomNumber2
                            )
                )
                )
                break
            except:
                print(
                    "That is an invalid answer, try again."
                )
                continue
        # noinspection PyTypeChecker
        if studentGuess == operator[self.randomSign](self.randomNumber1,
                                                     self.randomNumber2
                                                     ):
            print(
                "Correct."
            )
            self.studentScore += 1
        else:
            print(
                "Incorrect."
            )
