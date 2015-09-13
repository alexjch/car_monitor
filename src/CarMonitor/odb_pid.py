__author__ = 'alexjch'


class ODBPID(object):

    RPM =   "01 0C 2"
    SPEED = "01 0D 1"
    FUEL_LEVEL = "01 2F 1"
    BAROM_PRESSURE = "01 33 1"
    EXT_AIR_TEMP = "01 46 1"

    def __init__(self):
        object.__init__(self)