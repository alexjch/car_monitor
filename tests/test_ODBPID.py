__author__ = 'alexjch'

import unittest
from CarMonitor.odb_pid import ODBPID

class MyTestCase(unittest.TestCase):
    def test_something(self):
        odb_pid = ODBPID()
        self.assertEqual(odb_pid.RPM, "01 0C 2")


if __name__ == '__main__':
    unittest.main()
