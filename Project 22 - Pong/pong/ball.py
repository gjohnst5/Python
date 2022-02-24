from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def start_over(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.paddle_hit()


