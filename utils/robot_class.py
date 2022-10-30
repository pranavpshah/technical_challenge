
class Robot:

    def __init__(self, index):
        """
        Constructor for class Robot.
        Store important parameters for each robot
        Input:
            index (int) : index of robot
        Parameters:
            self.index (int) : index of robot
            self.curr_pos (list) : list of current position of robot [x,y,z,yaw,pitch,roll]
            self.destination : variable to store goal position in list form [x,y,z,yaw,pitch,roll]
            self.profile : variable that specifies the type of profile to use for bot's movement
        """
        self.index = index
        self.curr_pos = [0,0,0,0,0,0]
        self.destination = None
        self.profile = None
        
    def update_destination(self, destination, profile = 0):
        """
        function to update the destination position for robot and consequently the current position.
        (this function is assuming that the robot almost instanteousy performs the motion and reaches the destination)
        Input: 
            destination (list) : destination coordinates
            profile (int) : profile id
        """
        self.destination = destination
        self.curr_pos = self.destination
        self.profile = profile
