from .robot_class import Robot
from .stations_class import Station
import json
import pdb

class Commands:

    def __init__(self, robot_obj):
        """
        Constructor for Commands class. 
        Input:
            robot_obj (class object) : Class object of Robot class
        Parameters:
            self.robot (class object) : robot_obj
            self.station (class object) : class object of class Station
            self.reply_msg : variable to store the reply messages after each command
        """
        self.robot = robot_obj
        self.station = Station()
        self.reply_msg = None

    def in_msg(self, command):
        """
        Function that processes the input commands.
        Input: 
            command (string) : A string with all the arguments of the commands
        """

        cmd_ls = command.split()    # command split into a list of words
        length = len(cmd_ls)
        done = False    #flag to check if a command has been executed. 
        # flag is to allow checking of conditions of only 1 command.

        if(len(cmd_ls) > 1):
            # bank of commands where the input words are more than 1

            if((cmd_ls[0] == "movec" or cmd_ls[1] == "move") and not done):
                done = True
                if(cmd_ls[0] != "1" and not done):
                    self.reply_msg = "Invalid robot index"
                else:
                    if(cmd_ls[1] == "move"):    
                        """
                        block to execute the move command.
                        To move the robot to a certian station.
                        syntax : robot_id move station_index profile_index
                        """
                        station = int(cmd_ls[2])
                        if(station > len(self.station.station_map)):
                            self.reply_msg = "Invalid station index"
                        elif(length != 4):
                            self.reply_msg = "Invalid syntax"
                        else:
                            self.robot.update_destination(self.station.station_map[station], int(cmd_ls[3]))
                            # self.reply_msg = "1 0"
                            self.reply_msg = "Executed move"

                    elif(cmd_ls[0] == "movec"):     
                        """
                        block to execute movec command.
                        To move the robot to some specified location.
                        syntax : movec profile_id x y z yaw pitch roll
                        """
                        if(length != 8):
                            self.reply_msg = "Invalid syntax"
                        else:
                            profile = [cmd_ls[1]]
                            coord = [int(cmd_ls[2]), int(cmd_ls[3]), int(cmd_ls[4]), int(cmd_ls[5]), int(cmd_ls[6]), int(cmd_ls[7])]
                            self.robot.update_destination(coord, profile)
                            # self.reply_msg = "1 0"
                            self.reply_msg = "Executed movec"

            if(cmd_ls[0] == "loc" and not done):
                """
                block to execute loc command.
                To get the coordinates of a station.
                syntax : loc station_index
                """
                done = True
                station = int(cmd_ls[1])
                if(length != 2):
                    self.reply_msg = "Invalid syntax"
                elif(int(cmd_ls[1]) > len(self.station.station_map)):
                    self.reply_msg = "Invalid station index"
                else:
                    self.reply_msg = "Location of station " + cmd_ls[1] + " is " + str(self.station.station_map[station])
                    # self.reply_msg = "0 " + cmd_ls[1] + " " + str(self.station.station_map[station])

            if(cmd_ls[0] == "locxyz" and not done):
                """
                block to execute locxyz command.
                To update the coordinates of a station.
                syntax : locxyz station_index x y z yaw pitch roll
                """
                done = True
                station = int(cmd_ls[1])
                if(int(cmd_ls[1]) > len(self.station.station_map)):
                    self.reply_msg = "Invalid station index"
                else:
                    self.station.station_map[station] = [int(cmd_ls[2]), int(cmd_ls[3]), int(cmd_ls[4]), int(cmd_ls[5]), int(cmd_ls[6]), int(cmd_ls[7])]
                    # self.reply_msg = "0 " + cmd_ls[1] + " " + str(self.station.station_map[station])
                    self.reply_msg = "Location of station " + cmd_ls[1] + " updated"
                    # pdb.set_trace()

            if(cmd_ls[0] == "teachplate" and not done):
                """
                block to execute teachplate command
                To teach the robot the location of a station.
                syntax : teachplate station_index
                """
                done = True
                self.station.station_map[int(cmd_ls[1])] = self.robot.curr_pos
                # self.reply_msg = "1 0"
                self.reply_msg = "Location of station " + cmd_ls[1] + " updated"
                # pdb.set_trace

            if(cmd_ls[0] == "pickplate" and not done):
                """
                block to execute pickplate command
                To make the bot move to a station and perform the picking maneuver.
                syntax : pickplate station_index
                """
                done = True
                self.robot.update_destination(self.station.station_map[int(cmd_ls[1])])
                # self.reply_msg = "1"    #return 0 for plate not successfully held
                self.reply_msg = "Plate picked"

            if(cmd_ls[0] == "placeplate" and not done):
                """
                block to execute placeplate command
                To make the bot move to a station and perform the placing maneuver.
                syntax : placeplate station_index
                """
                done = True
                self.robot.update_destination(self.station.station_map[int(cmd_ls[1])])
                # self.reply_msg = "1"
                self.reply_msg = "Plate placed"
        
        else:
                
            if(cmd_ls[0] == "destc" and not done):
                """
                block to execute destc command
                To get the coordinates of the current goal destination of the bot.
                syntax : destc
                """
                done = True
                if(self.robot.destination):
                    self.reply_msg = "Current goal destination is " + str(self.robot.destination)
                else:
                    self.reply_msg = "No destination given yet"
                
            if(cmd_ls[0] == "wherec" and not done):
                """
                block to execute wherec command
                To get the current position coordinates of the bot.
                syntax : wherec
                """
                done = True
                self.reply_msg = "Current position is " + str(self.robot.curr_pos)

        
        if(not done):
            """
            If none of the commands were executed above, then a wrong command was entered.
            """
            self.reply_msg = "Invalid command"
        
