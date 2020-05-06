# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 
# The numbers after the direction are steps. Write a program to compute the distance from current position
# after a sequence of movement and original point. If the distance is a float, 
# then just print the nearest integer. Example: If the following tuples are given as input to the program:
# UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2
import math

def move(startPos, up, down, left, right):
    y = up - down
    x = left - right
    
    newx = startPos[0] + x
    newy = startPos[1] + y

    return (x, y)

def distance(startPos, newPos):
    x = startPos[0] - newPos[0]
    y = startPos[1] - newPos[1]

    distance = math.sqrt((x*x) + (y*y))
    return round(distance)

startPos = (0, 0)
newPos = move(startPos, 5, 3, 3, 2)

print(newPos)
print(distance(startPos, newPos))