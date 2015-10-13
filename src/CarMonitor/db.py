__author__ = 'alexjch'

import os
import sqlite3


CREATE_DB = '''CREATE TABLE telemetry (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                       STREAM TEXT,
                                       Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)'''

DB_INSERT = '''INSERT INTO telemetry (STREAM) values("?")'''

DB_SELECT = '''SELECT * FROM telemetry order by Timestamp LIMIT 100'''


class DB(object):
    """ Database object abstraction that provides storage for data
        comming from connector"""

    def __init__(self, db_file="ODB.sqlite"):
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_file)
        self.conn = sqlite3.connect(db_path)
        self.conn.isolation_level = None
        self.db = self.conn.cursor()
        if not os.path.exists(db_path):
            self.db.execute(CREATE_DB)
            self.db.commit()

    def insert(self, stream):
        self.db.execute(DB_INSERT, (stream,))

    def extract(self):
        self.db.execute(DB_SELECT, ())
        return self.db.fetchall()

    def close(self):
        self.db.close()
        self.conn.close()
