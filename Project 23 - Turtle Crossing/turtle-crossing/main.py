import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

manager = CarManager()
player_turtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    manager.gen_car()
    manager.move_cars()

    for car in manager.cars:
        if car.distance(player_turtle) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player_turtle.is_finished():
        player_turtle.goto_start()
        manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
