import turtle as t

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.gen_snake()
        self.head = self.segments[0]

    def gen_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, pos):
        new_turtle = t.Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.segments.append(new_turtle)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
