import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        # reduce size by half. Default turtle size is 20px by 20px
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.penup()
        self.goto_new_posistion()

    def goto_new_posistion(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
