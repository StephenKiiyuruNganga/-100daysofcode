from turtle import Turtle


FORWARD_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.__default_length = 3
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for idx in range(self.__default_length):
            new_square = Turtle(shape="square")
            new_square.penup()

            # change look of head
            if idx == 0:
                new_square.color("green")
            else:
                new_square.color("white")

            # gap between coordinates should be 20px
            new_square.goto(x=-(idx * 20), y=0)
            self.segments.append(new_square)

    def add_segment(self):
        last_position = self.segments[-1].position()
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(last_position)
        self.segments.append(new_square)

    def forward(self):
        # range(start=2, stop=0, step=-1) => counts in this sequence => 2,1,0
        for idx in range(len(self.segments)-1, 0, -1):
            # get coordinates of the previous segment
            current_x = self.segments[idx - 1].xcor()
            current_y = self.segments[idx - 1].ycor()
            # move the current segment to the position of the previous
            self.segments[idx].goto(x=current_x, y=current_y)

        # move the head to a new position
        self.head.forward(FORWARD_DISTANCE)

    def up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(RIGHT)
