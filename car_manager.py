from turtle import Turtle
import random as rnd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance= rnd.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(rnd.choice(COLORS))
            y_pos=rnd.randint(-250,250)
            new_car.goto(300,y_pos)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car1 in self.all_cars:
          car1.forward(self.car_speed)

    #Speed up the car movement
    def level_up(self):
        self.car_speed += MOVE_INCREMENT



