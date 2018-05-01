from threading import Thread
from subprocess import call
from Classes.MathsQuiz import MathsQuiz
from Classes.Mongo import Mongo


class App(object):

    def __init__(self):
        self.userInput = 0
        self.uniqueID = 0
        self.studentName = 0
        self.studentScore = 0
        self.mongod_startup()
        
    def mongod_startup(self):
        mongodStartup = Thread(target=lambda :call("mongodb_startup.bat"))
        mongodStartup.start()

    def option_listing(self):
        print("Please choose one of the options below.\n\n"
          "If you would like to use the Maths Quiz, type '1'\n"
          "If you would like to read existing records, type '2'\n"
          "If you would like to read all existing records, type '3'\n"
          "If you would like to modify existing records, type '4'\n"
          "If you would like to delete existing records, type '5'\n"
          "If you would like to delete the entire database, type '6'\n"
          "If you would like to exit the program, type '7'\n"
              )
        self.userInput = str(input("Please choose one of the listed options: "))
        if self.userInput == "1":
            self.start_maths_quiz()
            self.option_listing()

        elif self.userInput == "2":
            self.uniqueID = str(input("What is your uniqueID: "))
            self.define_mongo()
            self.mongo.read_from_database()
            self.option_listing()

        elif self.userInput == "3":
            self.define_mongo()
            self.mongo.list_all_records()
            self.option_listing()

        elif self.userInput == "4":
            self.uniqueID = str(input("What is your uniqueID: "))
            self.studentScore = int(input("What is your score? "))
            self.define_mongo()
            self.mongo.overwrite_score_from_database()
            self.option_listing()
            
        elif self.userInput == "5":
            self.uniqueID = str(input("What is your uniqueID: "))
            self.define_mongo()
            self.mongo.delete_from_database()
            self.option_listing()

        elif self.userInput == "6":
            self.define_mongo()
            self.mongo.delete_entire_database()
            self.option_listing()

        elif self.userInput == "7":
            pass

        else:
            print("Thats an invalid input, please try again.")
            self.option_listing()

    def define_mongo(self):
        self.mongo = Mongo(self.uniqueID, self.studentName, self.studentScore)
        
    def start_maths_quiz(self):
        print(
            "In this basic Maths Quiz,"
            "You'll answer each question,"
            "& at the end you will get a score,"
            "which will be stored on a database.\n\n"
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
            mathsQuiz = MathsQuiz()
        else:
            pass

        
test = App()
test.option_listing()
