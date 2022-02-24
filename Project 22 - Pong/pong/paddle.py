from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def up(self):
        if self.ycor() < 250:
            y_cor = self.ycor() + 20
            self.goto(self.xcor(), y_cor)

    def down(self):
        if self.ycor() > -250:
            y_cor = self.ycor() - 20
            self.goto(self.xcor(), y_cor)



