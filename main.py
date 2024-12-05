import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

level = Scoreboard()
turtle = Player()
car = CarManager()

screen.onkey(turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Detecting if the turtle crossed the road or not
    if turtle.level_up() == True:
        turtle.starting_position()
        level.increase_score()
        car.exeleration()
    
    car.add_car()
        
    #Detect collision
    for a in car.cars_list:
        if turtle.distance(a) < 20:
            game_is_on = False
            level.game_over()



screen.exitonclick()
    
        

    
