from pymongo import MongoClient
from pprint import pprint


class Mongo(object):
    def __init__(self, unique_id, student_name, student_score  ):
        self.uniqueID = unique_id
        self.studentName = student_name
        self.studentScore = student_score
        self.client = MongoClient()
        self.db = self.client.maths_quiz
        self.collection = self.db.studentScores

    def store_to_database(self):
        post_to_database = {"name": self.studentName,
                            "unique_id": self.uniqueID,
                            "score": self.studentScore}
        self.collection.insert_one(post_to_database)

    def read_from_database(self):
        pprint(self.collection.find_one({"unique_id": self.uniqueID}, {"_id": False}))

    def delete_from_database(self):
        self.db.collection.delete_one({"name": self.uniqueID})

    def delete_entire_database(self):
        self.client.drop_database("maths_quiz")

    def list_all_records(self):
        for record in self.collection.find():
            print(record)

    def overwrite_score_from_database(self):
        self.collection.update_one({"unique_id": self.uniqueID},
                                   {"$set": {"score": self.studentScore}}, upsert=False)


