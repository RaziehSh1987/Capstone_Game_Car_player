import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car = CarManager()
score_board=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")  # With parentheses (player.go_up()):If you include the parentheses, you're calling the go_up method right away.

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    #Detect collision with car
    for carr in  car.all_cars:
        if player.distance(carr)<25:
            game_is_on=False
            score_board.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score_board.increase_level()

screen.exitonclick()