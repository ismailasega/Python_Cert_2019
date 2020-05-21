# A Robot moves in a Plane starting from the origin point (0,0).
# The robot can move toward UP, DOWN, LEFT, RIGHT.
# The trace of Robot movement is as given following:UP 5DOWN 3LEFT 3RIGHT 2The numbers after directions are steps.
# Write a program to compute the distance current position after sequence of movements.

import math

position = [0,0]

rotations = {"UP":[0,1], "DOWN":[0,-1], "LEFT":[-1,0], "RIGHT":[1,0]}

input_value = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]

for i in input_value:
    position_value = i.split()
    mv = position_value[0]
    val = position_value[1]
    if mv in rotations and val.isnumeric():
        position[0] += rotations[mv][0]*int(val)
        position[1] += rotations[mv][1]*int(val)

# computing distance
distance = round(math.sqrt(position[0]**2 + position[1]**2))
print("Distance:", distance)
