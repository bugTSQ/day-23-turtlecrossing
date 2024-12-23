from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""
Create a turtle player that starts at the bottom of the screen and listen for the "Up"
 keypress to move the turtle north. If you get stuck, check the video walkthrough in 
 Step 3.
"""
class Player:
    def __init__(self):
        turtle = Turtle
        turtle.shape = "turtle"
        turtle.setposition = STARTING_POSITION
