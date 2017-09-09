from threading import *
from subprocess import *
from pymongo import *
from pprint import *
from Classes.MathsQuiz import MathsQuiz
from Classes.Mongo import Mongo

student_users = {}


def mongod_startup():
    call("mongodb-startup.bat")


def startup():
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
        studentName = str(input(
            "What is your name? "
        )
        )
        student_users[studentName] = MathsQuiz(studentName)
        student_users[studentName].start_quiz()
    else:
        quit()


mongodStartup = Thread(target=mongod_startup)
mongodStartup.start()
startup()
