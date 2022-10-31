from utils.test_telnet import TestTelnet
import pdb

# from telnetlib import Telnet

## can take these arguments as user inputs
host = "192.168.0.1"
port_num = 10100

# with Telnet(host = host, port = port_num) as tn:
#     tn.interact()

flag = True
tn = TestTelnet()
connection = False  #flag too not make repeat connections

while(flag):

    ##establishing connection with the robot
    if(not connection):
        if(tn.open(host, port_num)):
            connection = True
            print("Connection successful\n")
    elif(not connection):
        print("Connection unsuccessful.\nTry again.\n")
        flag = False

    if(connection):
        # procedure to take a user command and se telnet to interact with bot
        command =  input("Enter command: ")
        if(command.lower() == "exit"):
            flag = False
            tn.close()
            print("Exiting...")
        else:
            tn.write(command.lower())
            print(tn.read_all())
            # actual telnet would use tn.read_all()
