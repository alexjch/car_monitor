
from exceptions import Exception

class DecodeException(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return "Unable to decode exception"

def remove_space(value):
    return value.replace(" ", "")

def h2i(value_str):
    return int("0x{}".format(value_str), 16)

def mask(value, length):
    return value & int("0x0{}".format("".join(['F' for i in range(0, length)])), 16)

"""Helper method that checks returning header and strips it"""
def decode_odb_msg(odb_request, odb_response):
    ack = h2i(remove_space(odb_response)) >> (len(remove_space(odb_response))*4 - 16)
    req, resp = map(h2i, map(remove_space, [odb_request, odb_response]))
    if req & ack == req:
        length = len(remove_space(odb_response)) - 4
        return mask(resp, length)

    raise DecodeException()

    

