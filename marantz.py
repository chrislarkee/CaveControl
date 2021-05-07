#a tool to remotely control a Marantz SR5008 audio receiver using its network interfaces. This is the command-line utility that works as a back-end to a GUI.

import telnetlib
from sys import exit
from sys import argv

def transmit(request):
    #translate friendly commands into the API's language
    if request == "reset":
        command = "MV600\r".encode('ascii')
    elif request == "ping":
        command = "PW?\r".encode('ascii')
    else:
        command = (request.upper()).encode('ascii')
    
    statusreport = "Command: " + request + "\n"
    tn = telnetlib.Telnet()
    try:
        tn.open('172.22.1.50', 23, 5)
        tn.write(command)
        statusreport += tn.read_very_eager().decode('ascii')
    except:
        statusreport += "error!\n"
    tn.close()
    return statusreport

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
