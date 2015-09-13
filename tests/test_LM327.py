__author__ = 'alexjch'

from unittest import TestCase
from CarMonitor.lm327 import LM327

class TestLM327(TestCase):

    def test_echo_off_code(self):
        lm327 = LM327()
        self.assertEqual(lm327.ECHO_OFF, "E0", "")

    def test_format_code(self):
        lm327 = LM327()
        self.assertEqual(lm327.form_at_cmd(lm327.ECHO_OFF), "AT E0", "")
