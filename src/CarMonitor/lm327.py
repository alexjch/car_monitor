__author__ = 'alexjch'



class LM327(object):

    # AT
    ECHO_ON = "E1"
    ECHO_OFF = "E0"
    IGNITION = "IGN"
    WARM_START = "WS"
    RESET = "Z"
    VOLTAGE = "RV"

    def __init__(self):
        object.__init__(self)

    def form_at_cmd(self, cmd):
        return "AT {cmd}".format(cmd=cmd)



