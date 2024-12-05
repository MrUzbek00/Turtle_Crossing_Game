from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

car = CarManager()
class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
    
    def move(self):
        self.forward(10)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        return self.ycor() > FINISH_LINE_Y
            # self.goto(STARTING_POSITION)
            # level.increase_score()
            # car.exeleration()
            
        
