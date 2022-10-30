import numpy as np
from .robot_class import Robot
from .commands import Commands

class TestTelnet:

    def __init__(self):
        """
        Constructor for TesTelnet.
        Parameters:
            self.host (string) : IP address
            self.port (int) : port number
            self.robot : variable that will be used to store the class object of class Robot
            self.cmd : variable that will be used to store the class object of class Commands
        """
        self.host = "192.168.0.1"
        self.port = 10100
        self.robot = None
        self.cmd = None

    def open(self, host, port):
        """
        Function to establish a connection for the specified the IP address and port number.
        Returns True if connection established else False
        Input:
            host (string) : IP address
            port (int) : port number
        """
        if(self.host == host and self.port == port):
            index = (self.port%100)//100
            self.robot = Robot(index)
            self.cmd = Commands(self.robot)
            return True
        else:
            return False
    
    def close(self):
        """
        Function that closes the connection
        """
        self.robot = None
        print("Connection closed.")

    def write(self, command):
        """
        Function that sends a command to the robot
        Input:
            command (string)
        """
        self.cmd.in_msg(command)
    
    def read_all(self):
        """
        Function that reads a response from the robot
        Output:
            reply_msg (string) : reply message from the robot
        """
        return self.cmd.reply_msg
