import bluetooth as bt


def find_device(device_name):
    discovered = bt.discover_devices()
    target = [d for d in discovered if bt.lookup_name(d) == device_name]
    return target.pop() if len(target) else None
    
if __name__ == "__main__":
    print find_device("RN42-B961")
