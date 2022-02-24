from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto_start()

    def move_up(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)

    def is_finished(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)

