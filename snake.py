from turtle import Turtle
class Snake:

    TUR_POS = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.turtle_body = []
        self.create_snake()
        self.head = self.turtle_body[0]

    def create_snake(self):
        for pos in self.TUR_POS:
            self.add_body(pos)

    def add_body(self, pos):
        new_tur = Turtle("square")
        new_tur.color("white")
        new_tur.penup()
        new_tur.goto(pos)
        self.turtle_body.append(new_tur)

    def extend(self):
        self.add_body(self.turtle_body[-1].position())

    def move_body(self):
        for i in range(len(self.turtle_body) - 1, 0, -1):
            x = self.turtle_body[i - 1].xcor()
            y = self.turtle_body[i - 1].ycor()
            self.turtle_body[i].goto(x, y)
        self.head.forward(20)

    def right(self):
        deg = self.head.heading()
        if deg == 180:
            return
        self.head.seth(0)

    def left(self):
        deg = self.head.heading()
        if deg == 0:
            return
        self.head.seth(180)

    def up(self):
        deg = self.head.heading()
        if deg == 270:
            return
        self.head.seth(90)

    def down(self):
        deg = self.head.heading()
        if deg == 90:
            return
        self.head.seth(270)

