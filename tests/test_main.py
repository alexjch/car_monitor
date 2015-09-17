__author__ = 'alexjch'

import os
import unittest
from CarMonitor.main import parameters_file
from mock import Mock

btmock = Mock()
btmock.send = Mock(return_value = None)
btmock.receive = Mock(return_value = "00 00{}".format(chr(62)))

CODES_FILE = "codes.file"

class TestCaseMain(unittest.TestCase):

    @classmethod
    def setUpClass(TestCaseMain):
        fh = open(CODES_FILE, "w")
        fh.write("01 00 1\n")
        fh.write("01 00 1\n")
        fh.write("\n")
        fh.write("01 00 1\n")
        fh.write("\n")
        fh.write("\n")

    @classmethod
    def tearDownClass(TestCaseMain):
        os.unlink(CODES_FILE)

    def test_filter_empty_lines(self):
        for _ in parameters_file(CODES_FILE, btmock):
            self.assertTrue(btmock.send.call_count, 3)


if __name__ == '__main__':
    unittest.main()
