from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.print_score()

    def update(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0,280)
        self.write(f"Score = {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center")
