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
        print(
"""Please choose one of the options below.
If you would like to use the Maths Quiz, type '1'
If you would like to read existing records, type '2'
If you would like to read all existing records, type '3'
If you would like to modify existing records, type '4'
If you would like to delete existing records, type '5'
If you would like to delete the entire database, type '6'
If you would like to exit the program, type '7'""")
        self.userInput = str(input("Please choose one of the listed options: "))
        if self.userInput == "1": #Works
            self.start_maths_quiz()
            print("\n\n\n")
            self.option_listing()

        elif self.userInput == "2": #Works
            print("This will display your current score, name, and uniqueID.")
            self.verify_option()
            self.uniqueID = str(input("What is your uniqueID: "))
            self.define_mongo()
            self.mongo.read_from_database()
            print("\n\n\n")
            self.option_listing()

        elif self.userInput == "3": #Works
            print("This will display everyone's current score, name, and uniqueID.")
            self.verify_option()
            self.define_mongo()
            self.mongo.list_all_records()
            print("\n\n\n")
            self.option_listing()

        elif self.userInput == "4":
            print("This will modify your current score.")
            self.verify_option()
            self.uniqueID = str(input("What is your uniqueID: "))
            while True:
                try:
                    self.studentScore = int(input("What is your new score: "))
                    break
                except:
                    print("That is an invalid input. ")
                    continue
            self.define_mongo()
            self.mongo.overwrite_score_from_database()
            print("\n\n\n")
            self.option_listing()
            
        elif self.userInput == "5": #Works
            print("This will delete your entire record.")
            self.verify_option()
            self.uniqueID = str(input("What is your uniqueID: "))
            self.define_mongo()
            self.mongo.delete_from_database()
            print("\n\n\n")
            self.option_listing()

        elif self.userInput == "6":
            print("This will delete the entire database.")
            self.verify_option()
            self.define_mongo()
            self.mongo.delete_entire_database()
            print("\n\n\n")
            self.option_listing()

        elif self.userInput == "7":
            quit()

        else:
            print("Thats an invalid input, please try again.")
            self.option_listing()

    def define_mongo(self):
        self.mongo = Mongo(self.uniqueID, self.studentName, self.studentScore)
        
    def start_maths_quiz(self):
        print(
            "In this basic Maths Quiz,\n"
            "You'll answer each question,\n"
            "& at the end you will get a score,\n"
            "which will be stored on a database.\n\n"
        )
        self.verify_option()
        mathsQuiz = MathsQuiz()

    def verify_option(self):
        while True:
            quizOrQuit = input("Do you wish to select that option? (Y/N)").lower()
            if quizOrQuit not in "yes":
                if quizOrQuit not in "no":
                    print("Invalid input, please try again.")
                else:
                    break
            else:
                break
        if quizOrQuit != "" and quizOrQuit  in "yes":
            pass
        elif quizOrQuit != "" and quizOrQuit  in "no":
            quit()
        else:
            print("Invalid input, please try again.")
            self.verify_option()

        
test = App()
test.option_listing()
