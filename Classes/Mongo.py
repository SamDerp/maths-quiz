from pymongo import MongoClient
from pprint import pprint


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
