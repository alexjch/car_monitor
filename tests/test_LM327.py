__author__ = 'alexjch'

from unittest import TestCase
from CarMonitor.lm327 import LM327

from mock import Mock

btmock = Mock()
btmock.init_bus = Mock(return_value = "BE1FA813")


class TestLM327(TestCase):

    def test_echo_off_code(self):
        lm327 = LM327(btmock)
        self.assertEqual(lm327.ECHO_OFF, "E0", "")

    def test_format_code(self):
        lm327 = LM327(btmock)
        self.assertEqual(lm327.form_at_cmd(lm327.ECHO_OFF), "AT E0", "")

    def test_init_bus(self):
        lm327 = LM327(btmock)
        available_pids = lm327.init_bus()

