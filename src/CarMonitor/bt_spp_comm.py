__author__ = 'alexjch'
import signal
try:
    import bluetooth as bt
except:
    pass

BUFF_SIZE = 1024

def find_device(device_name):
    discovered = bt.discover_devices()
    target = [d for d in discovered if bt.lookup_name(d) == device_name]
    return target.pop() if len(target) else None


class BTAgent(object):
    """ Bluetooth agent, this object asbtracts communication with
        a bluetooth device.  This object is in charge of channel
        initialization and provides methods to send and receive
        data"""

    def __init__(self, dev_address, port=1):
        object.__init__(self)
        self.sock = bt.BluetoothSocket(bt.RFCOMM)
        self.sock.connect((dev_address, port))

    def receive(self):
        chunks = []
        receiving = 1
        while receiving:
            chunk = self.sock.recv(BUFF_SIZE)        
            chunks.append(chunk.replace("\r", "\n"))
            if chr(62) in chunk:
                return "".join(chunks)

    def send(self, msg):
        msg = "{}{}".format(msg, chr(13))
        return self.sock.send(msg)

    def close(self):
        self.sock.close()

    def __del__(self):
        self.close()



