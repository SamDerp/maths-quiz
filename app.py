from threading import *
from subprocess import *
from pymongo import *
from pprint import *
from Classes.MathsQuiz import MathsQuiz


student_users = {}


def mongod_startup():
    call("mongodb-startup.bat")


class Mongo(object):
    def __init__(self, studentName):
        self.studentName = studentName
        self.client = MongoClient()
        self.db = self.client.maths_quiz
        self.collection = self.db.studentScores

    def store_to_database(self):
        postToDatabase = {"name": self.studentName,
                          "score": student_users[self.studentName].studentScore}
        self.db.posts.insert_one(postToDatabase)

    def read_from_database(self):
        pprint(self.db.posts.find_one({"name": self.studentName}))

    def delete_from_database(self):
        self.db.posts.delete_one({"name": self.studentName})

    def overwrite_score_from_database(self):
        self.db.posts.update({"name": self.studentName},
                             {"$set": {"score": student_users[self.studentName].studentScore}})

    def delete_entire_database(self):
        self.client.db.command("dropDatabase")


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
