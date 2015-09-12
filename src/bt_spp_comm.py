import signal
import bluetooth as bt
from find_device import find_device

BUFF_SIZE = 1024


class BTAgent(object):

    def __init__(self, dev_address, port=1):
        object.__init__(self)
        self.sock = bt.BluetoothSocket(bt.RFCOMM)
        self.sock.connect((dev_address, port))

    def receive(self):
        chunks = []
        recv_count = 0
        while recv_count < BUFF_SIZE:
            chunk = self.sock.recv(BUFF_SIZE)        
            print chunk
            chunks.append(chunk)
            recv_count = recv_count + len(chunks)
        return "".join(chunks)

    def send(self, msg):
        msg = "{}\n".format(msg)
        return self.sock.send(msg)

    def close(self):
        self.sock.close()

    def __del__(self):
        self.close()

#
# X-Move input text code outside BTAgent
# X-Write reader thread code
# -Write DB 
# -Test ODBII
#

if __name__ == "__main__":
#    address = find_device("RN42-B961")
#    address = "00:06:66:45:B9:61" 
    address = "00:1D:A5:00:11:62" #ODBII
    bt = BTAgent(address)
    def sigint_handler(signal, frame):
        bt.close()
        print("\n")
        exit(0)
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        msg = raw_input("btagent# ")
        bt.send(msg)
        print "received: "
        print bt.receive()


