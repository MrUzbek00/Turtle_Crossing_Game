from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.setposition(-230, 230)
        self.score = 1
        self.update_score()
        
        
    
    def update_score(self):
        self.clear()
        print(f"Updating score to Level {self.score}")
        self.write(f"Level {self.score}", move=False, align="center", font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.setposition(0,0)
        self.write("Game Over", move=False, align="center", font=FONT)

    
