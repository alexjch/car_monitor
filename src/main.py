import sys
import signal
import argparse
from bt_spp_comm import BTAgent as bta
from find_device import find_device

def arguments_parser():
    ap = argparse.ArgumentParser(description="ODBII communication tool")
    device_id_group = ap.add_mutually_exclusive_group(required=True) 
    device_id_group.add_argument("--device_name", help="Name of the device to connect to", default=None)
    device_id_group.add_argument("--device_addr", help="Address of the device to connect to", default=None)
    ap.add_argument("-I", "--interactive", action="store_true", default=False, 
                    help="Interactive mode, in this mode the connection will stay \
                          open and the data that is typed in command line is send \
                          to the device")    
    return ap.parse_args()

def sigint_handler(signal, frame):
    print >> sys.stdout, "\n"    
    sys.exit(0)

def main(args):
    signal.signal(signal.SIGINT, sigint_handler)
    address = args.device_addr if args.device_addr is not None else find_device(args.device_name) 
    bt = bta(address)
    
    if args.interactive:
        while True:
            msg = raw_input("btagent# ")
            bt.send(msg)
            print("received: {}".format(bt.receive()))
        

if __name__ == "__main__":
    main(arguments_parser())

