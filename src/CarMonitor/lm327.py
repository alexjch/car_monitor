__author__ = 'alexjch'

PIDs = ["01", "02", "03", "04", "05", "06", "07", "08",
        "09", "0A", "0B", "0C", "0D", "0E", "0F", "10",
        "11", "12", "13", "14", "15", "16", "17", "18",
        "19", "1A", "1B", "1C", "1D", "1E", "1F", "20"]


class LM327(object):
    """ Abstraction that contains methods to talk to LM327 and ODB"""
    # AT commands
    ECHO_ON = "E1"
    ECHO_OFF = "E0"
    IGNITION = "IGN"
    WARM_START = "WS"
    RESET = "Z"
    VOLTAGE = "RV"

    def __init__(self, btcomm):
        object.__init__(self)
        self.btcomm = btcomm

    def init_bus(self):
        pass

    def form_at_cmd(self, cmd):
        return "AT {cmd}".format(cmd=cmd)




