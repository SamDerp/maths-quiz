from pymongo import MongoClient
from pprint import pprint


class Mongo(object):
    def __init__(self, uniqueID, studentName, studentScore):
        self.uniqueID = uniqueID
        self.studentName = studentName
        self.studentScore = studentScore
        self.client = MongoClient()
        self.db = self.client.maths_quiz
        self.collection = self.db.studentScores

    def store_to_database(self):
        postToDatabase = {"name": self.studentName,
                          "unique_id": self.uniqueID,
                          "score": self.studentScore}
        self.db.posts.insert_one(postToDatabase)

    def read_from_database(self):
        pprint(self.db.posts.find_one({"name": self.studentName}, {"_id": False}))

    def delete_from_database(self):
        self.db.posts.delete_one({"name": self.studentName})

    def overwrite_score_from_database(self):
        self.db.posts.update({"unique_id": self.uniqueID},
                             {"$set": {"score": self.studentScore}})
