import os
import sqlite3 as sql

class DbContext:
    def __init__(self):
        db_folder = '../Database'
        db_file = 'mnk_base.db'
        db_path = os.path.join(db_folder, db_file)

        if not os.path.exists(db_folder):
            os.makedirs(db_folder)

        self.db = sql.connect(db_path)
        self.cursor = self.db.cursor()

