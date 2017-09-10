from threading import *
from subprocess import *
from Classes.MathsQuiz import MathsQuiz
from Classes.Mongo import Mongo


class Startup(object):
    def __init__(self):
        self.MathsQuiz = 0
        self.Mongo = 0

    def startup_maths_quiz(self):
        print(
            "This is a basic Maths quiz,"
            "answer each question,"
            "at the end you will get a score.\n\n"
        )
        while True:
            quizOrQuit = input(
                "Do you wish to participate? (Y/N)"
            ).lower()
            if quizOrQuit not in "yesno":
                print(
                    "Not a valid input."
                )
            else:
                break
        if quizOrQuit in "yes":
            self.MathsQuiz = MathsQuiz()
            self.MathsQuiz.startup()
        else:
            quit()

    def call_mongo(self):
        self.Mongo = Mongo(self.MathsQuiz.uniqueID, self.MathsQuiz.studentName, self.MathsQuiz.studentScore)


def mongod_startup():
    call("mongodb_startup.bat")


mongodStartup = Thread(target=mongod_startup)
mongodStartup.start()

Startup = Startup()
Startup.startup_maths_quiz()
Startup.call_mongo()
