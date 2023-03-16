import datetime

from Services.Db.MongoDbService import MongoDbService as mongo


class Logger:
    @staticmethod
    def log(log_type, log_message):
        date_stamp = datetime.date.today()
        time_stamp = datetime.datetime.now().strftime("%H:%M:%S")

        log = {
            'date': date_stamp,
            'time': time_stamp,
            'type': log_type,
            'message': log_message
        }

        print(f'({date_stamp}\t{time_stamp})\t{log_type}\t|\t{log_message}')
        mongo.insert_log(log)


Logger.log('SUCCESS', 'Testing mongo db')
