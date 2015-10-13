__author__ = 'alexjch'
import sys
import time
import signal
import argparse
from bt_spp_comm import BTAgent as bta, find_device

SLEEP_TIME = 5

def arguments_parser():
    ap = argparse.ArgumentParser(description="ODBII communication tool")
    device_id_group = ap.add_mutually_exclusive_group(required=True) 
    device_id_group.add_argument("--device_name", help="Name of the device to connect to", default=None)
    device_id_group.add_argument("--device_addr", help="Address of the device to connect to", default=None)
    op_mode_group = ap.add_mutually_exclusive_group(required=True)
    op_mode_group.add_argument("-I", "--interactive", action="store_true", default=False,
                               help="Interactive mode, in this mode the connection will stay \
                               open and the data that is typed in command line is send to the \
                               device")
    op_mode_group.add_argument("-F", "--parameters_file", default=None,
                               help="File with a list of parameters to read from vehicle")
    op_mode_group.add_argument("-L", "--listening", default=False,
                               help="Puts the LM327 in listening mode to monitor traffic on \
                               the can bus")
    ap.add_argument("-C", "--continuous", default=False, action="store_true", help="Do it until CTRL^C", type=int)
    ap.add_argument("-D", "--data_base", default="odb")

    return ap.parse_args()


def sigint_handler(signal, frame):
    print >> sys.stdout, "\n"    
    sys.exit(0)


def interactive_mode(bt):
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        msg = raw_input("btagent# ")
        bt.send(msg)
        print("received: {}".format(bt.receive()))


def parameters_file(file_name, bt):
    with open(file_name) as input:
        parameters = filter(lambda x: x != "", input.read().split("\n"))
        for parameter in parameters:
            bt.send(parameter)
            yield bt.receive()


def continuous_parameters_file(file_name, bt):
    while True:
        for _ in parameters_file(file_name, bt):
            print _
            time.sleep(SLEEP_TIME)


def monitor_bus(bt):
   pass


def main(args):
    address = args.device_addr \
        if args.device_addr is not None else find_device(args.device_name)

    bt = bta(address)

    if args.interactive:
        interactive_mode(bt)
    elif args.continuous and args.parameters_file:
        continuous_parameters_file(args.parameters_file, bt)
    elif args.parameters_file:
        parameters_file(args.parameters_file, bt)
    elif args.listening_mode:
        monitor_bus(bt)

if __name__ == "__main__":
    main(arguments_parser())

