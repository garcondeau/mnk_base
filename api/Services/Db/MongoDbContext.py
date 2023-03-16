from pymongo import MongoClient

class MongoDbContext:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['logs_db']
        self.logs = self.db['logs']
