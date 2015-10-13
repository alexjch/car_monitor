__author__ = 'alexjch'

import os
import unittest
from CarMonitor.db import DB

DB_FILE = "test.sqlite"
DB_PATH = os.path.join(os.path.abspath("../"), "src" ,"CarMonitor",DB_FILE)

class MyTestCase(unittest.TestCase):

    def test_db_file_creation(self):
        db = DB(DB_FILE)
        self.assertTrue(os.path.exists(DB_PATH))
        db.close()
        os.unlink(DB_PATH)

    def test_insert_element(self):
        db = DB(DB_FILE)
        for n in range(0, 100):
            db.insert("1209 03940 94056")
        rows = db.extract()
        self.assertEqual(len(rows), 100)
        db.close()
        os.unlink(DB_PATH)


if __name__ == '__main__':
    unittest.main()
