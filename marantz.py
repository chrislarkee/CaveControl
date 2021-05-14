#a tool to remotely control a Marantz SR5008 audio receiver using its network interfaces. This is the command-line utility that works as a back-end to a GUI.

import telnetlib
from sys import exit
from sys import argv

MARANTZ_IP = '172.22.1.50'

def transmit(request):
    #translate friendly commands into the API's language
    if request == "reset":
        command = "MV400\r".encode()
    elif request == "ping":
        command = "PW?\r".encode()
    else:
        command = (request.upper() + "\r").encode()
    
    statusreport = "Transmitting: " + request + "\n"
    tn = telnetlib.Telnet()
    try:
        tn.open(MARANTZ_IP, 23, 5)
        tn.write(command)
    except:
        statusreport += "Unable to open connection.\n"
    try:
        statusreport += "Response: " + tn.read_until(b'\r', timeout=5).decode()
    except:
        statusreport += "No response.\n"
    tn.close()
    return statusreport

def startup():
    status = {
        "power": False,
        "volume": 400
    }
    tn = telnetlib.Telnet()
    try:
        tn.open(MARANTZ_IP, 23, 2)
    except:
        print("No Connection to audio receiver.")
        return status
    #power
    tn.write("PW?\r".encode())
    response = tn.read_until(b'\r', timeout=5).decode()
    if "ON" in response:
        status["power"] = True
    
    #startup volume
    tn.write("MV400\r".encode())
    tn.close()   
    return status    

def printHelp():
    print("Valid Commands:",\
        "PWON\t\tTurn on audio receiver",\
        "PWSTANDBY\tTurn off audio receiver",\
        "MV00\t\tMain volume: 0",\
        "MVUP\t\tMain volume: up",\
        "MVDOWN\t\tMain volume: down",\
        "reset\t\tRestore volume to default",\
        "ping\t\tQuery power state",sep='\n ')
    exit(0)

if __name__ == '__main__':
    if len(argv) == 1: 
        printHelp()
    
    #ok go
    print(transmit(argv[1]))
    exit(0)
