from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def gen_car(self):
        if random.randint(1, 6) == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT



