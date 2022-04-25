from turtle import Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn off autorefreshing of graphics on screen
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen for key strokes
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    # delay graphics by 0.1sec
    time.sleep(0.1)

    # move the snake forward
    snake.forward()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        food.goto_new_posistion()
        snake.add_segment()

    # detect collision with wall
    if abs(snake.head.xcor()) > 295 or abs(snake.head.ycor()) > 295:
        game_is_on = False
        scoreboard.game_over()

    # detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
