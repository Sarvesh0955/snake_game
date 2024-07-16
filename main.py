from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake1 = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move_body()

    if snake1.head.distance(food) < 15:
        snake1.extend()
        food.rand_pos()
        scoreboard.update()

    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for seg in snake1.turtle_body:
        if snake1.head == seg:
            pass
        elif snake1.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.update()

screen.exitonclick()
