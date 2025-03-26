from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle): #creates player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)


    def move_up(self): #turtle moves forward
        self.forward(MOVE_DISTANCE)

    def reset_player(self): #turtle resets back to original position
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)


