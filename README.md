# technical_challenge
The main file is `sandbox.py` which will act as our interface with the robot. The files in the folder `utils` are to simulate what the interaction with the robot might look like. Certain set of commands have been coded for this simulation, the details of which are given below.

# Commands

`move`:
To move the robot to a certian station.
Syntax:
```
robot_id move station_id profile_id
```

`movec`:
To move the robot to some specified location.
Syntax:
```
movec profile_id x y z yaw pitch roll
```

`loc`:
To get the coordinates of a station.
Syntax:
```
loc station_id
```

`locxyz`:
To update the coordinates of a station.
Syntax:
```
locxyz station_id x y z yaw pitch roll
```

`teachplate`:
To teach the robot the location of a station.
Syntax:
```
teachplate station_id
```

`pickplate`:
To make the bot move to a station and perform the picking maneuver.
Syntax:
```
pickplate station_id
```

`placeplate`:
To make the bot move to a station and perform the placing maneuver.
Syntax:
```
placeplate station_id
```

`destc`:
To get the coordinates of the current goal destination of the bot.
Syntax:
```
destc
```

`wherec`:
To get the current position coordinates of the bot.
Syntax:
```
wherec
```

# utils 

### test_telnet.py
A python script to simulate the `Telnet` class. Since it was not possible to connect to an actual network and interact, I made a simple file that would help me see what the interface looks like.

### commands.py
File which process the commands entered by the user and provides a reply.

### robot_class.py
A Class of the robot which stores the parameters, destination and current position of the robot. A new class object can be instantiated for each new robot.

### stations_class.py
Stores the location of each station.


# Sample Output

image.png

