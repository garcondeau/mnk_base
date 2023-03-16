from Services.Db.MongoDbContext import MongoDbContext

class MongoDbService:
    @staticmethod
    def insert_log(log):
        mongo = MongoDbContext()
        mongo.logs.insert_one(log)
