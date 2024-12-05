from turtle import Turtle
from random import randint,randrange,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.cars_list = []
        

    def add_car(self):
        if randint(1,5) == 5:
            new_car = self.car()
            if isinstance(new_car,Turtle):  # Only append if a car was actually created
                self.cars_list.append(new_car)
        self.car_move()

    def car(self):

        new_car = Turtle()
        new_car.penup()
        y_cor = randrange(-250, 250, 10)
        new_car.setposition(250, y_cor)
        new_car.shape("square")
        new_car.color(choice(COLORS))
        new_car.resizemode(rmode="user")
        new_car.shapesize(stretch_wid=0.5, stretch_len=1)
        new_car.setheading(180)
        return new_car
        
    def car_move(self):
        for car in self.cars_list:
            car.forward(self.starting_move_distance)
        
    def exeleration(self):
        self.starting_move_distance += 10
        
    
     
        

