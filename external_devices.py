import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

def get_ports():
    devices={}
    for port, description, hardwareIdentification in ports:
        portData = {
            'port' : port,
            'description' : description, 
            'hwid' : hardwareIdentification
        }
        devices[port] = portData

    return devices

if __name__ == '__main__':
    print(list(get_ports().keys()))

