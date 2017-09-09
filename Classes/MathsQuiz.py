from random import randint, choice
from operator import add, mul, sub


class MathsQuiz(object):
    def __init__(self, studentName):
        self.studentName = studentName
        self.randomNumber1 = 0
        self.randomNumber2 = 0
        self.randomSign = 0
        self.studentScore = 0

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
