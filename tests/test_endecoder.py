__author__ = 'alexjch'

import unittest
from CarMonitor.decoder import (decode_odb_msg as decode_msg,
                                DecodeException)

class TestCaseMain(unittest.TestCase):

    def test_decode_line(self):
        REQUEST = "01 05"
        RESPONSE = "41 05 7b"

        msg = decode_msg(REQUEST, RESPONSE)
        self.assertEqual(msg, int("0x" + RESPONSE[-2:], 16))

    def test_decode_exception(self):
        REQUEST = "01 05"
        RESPONSE = "41 06 30"

        try:
            msg = decode_msg(REQUEST, RESPONSE)
            self.assertTrue(False, "Did not produce an exception")
        except DecodeException as de:
            self.assertTrue(True, "Exception handled properly")

    def test_01_00(self):
        REQUEST = "01 00"
        RESPONSE = "41 00 BE 1F B8 10"

        msg = decode_msg(REQUEST, RESPONSE)
        self.assertEqual(msg, int("0xBE1FB810", 16))


if __name__ == '__main__':
    unittest.main()
