#a tool to remotely control a group of Christie WU7K-M projectors using their network interfaces. This is the command-line utility that works as a back-end to a GUI.

import socket
from sys import exit, argv
from threading import Thread, active_count
from time import sleep

global statusreport
statusreport = ""

def transmit(request):
    #translate friendly commands into the API's language
    if request == "on":
        command = "($PWR1)"
    elif request == "off":
        command = "($PWR0)"
    elif request == "open":
        command = "(#SHU0)"
    elif request == "close":
        command = "(#SHU1)"
    elif request == "3d":
        command = ""
    elif request == "3d_old":
        command = "($TDM+MAIN2)"
    elif request == "2d":
        command = "(#TDM+MAIN0)"
    elif request == "floorOn":
        command = "($9PWR1)($10PWR1)"
    elif request == "floorOff":
        command = "($9PWR0)($10PWR0)"
    elif request == "ping":
        command = "(#PWR?)"
    elif request == "test":
        command = "($9PWR?)($10PWR?)"
    else:
        print("Command not found.")
        exit(127)

    global statusreport
    statusreport = ""
    if request == "3d":
        for projector in range(1, 9):
            thr = Thread(target=transmitThread, args=(projector, "(#TDM+MAIN5)"))
            thr.start()
        for projector in range(9, 11):
            thr = Thread(target=transmitThread, args=(projector, "(#TDM+MAIN0)"))
            thr.start()
    else:
        for projector in range(1, 11):
            thr = Thread(target=transmitThread, args=(projector, command))
            thr.start()
        
    while active_count() > 1:
        sleep(0.2)
    #statusreport += "Transmission complete."
    return statusreport
                
def transmitThread(id, command):
    #your lab's IPs will vary
    ip = "172.22.1.1" + str(id).zfill(2)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(8.0)
    global statusreport
    try:
        s.connect((ip, 3002))
        s.send(command.encode())
        response = s.recv(1024)
        statusreport += ip + ": " + response.decode() + "\n"
    except socket.timeout:
        statusreport += ip + ": timed out.\n"
    s.close()
    
def startup():
    status = {
        "power": False,
        "shutter": False
    }
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    try:
        s.connect("172.22.1.101", 3002)
    except:
        print("No Connection to projectors.")
        return status 
    #power
    s.send("(#PWR?)".encode())
    response = s.recv(1024).decode()
    if "ON" in response:
        status["power"] = True

    #shutters
    s.send("(#SHU?)".encode())
    response = s.recv(1024).decode()
    if "OPEN" in response:
        status["shutter"] = True
    
    s.close
    return status   

def printHelp():
    print("Valid Commands:",\
        "on\t\tTurn on all projectors",\
        "off\t\tTurn off all projects",\
        "open\t\tOpen shutters (unmute video)",\
        "close\t\tClose shutters (mute video)",\
        "floorOn\tEnable floor projectors",\
        "floorOff\tDisable floor projectors",\
        "3d\t\tEnable top-bottom stereo",\
        "3d_old\tEnable frame doubled stereo",\
        "2d\t\tDisable stereo",
        "ping\t\tQuery power state",sep='\n ')
    exit(0)

if __name__ == '__main__':
    if len(argv) == 1: 
        printHelp()
    
    #ok go
    print(transmit(argv[1]))
    exit(0)
