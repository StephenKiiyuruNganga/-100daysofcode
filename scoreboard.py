from turtle import Turtle

FONT = ("Courier", 17, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_data()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_text(
            text=f"Score: {self.score} | High Score: {self.high_score}", x_cor=0, y_cor=260)

    def write_text(self, text, x_cor=0, y_cor=0):
        """writes text on screen

        Arguments:
        :text: the text to be displayed
        :x_cor: x coordinate for the text. Default 0
        :y_cor: y coordinate for the text. Default 0
        """
        self.goto(x=x_cor, y=y_cor)
        self.write(text, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write_text(
            text=f"Score: {self.score} High Score: {self.high_score}", x_cor=0, y_cor=260)

    def game_over(self):
        self.write_text(text="😔😔 GAME OVER 😔😔")
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_data()

    def save_data(self):
        try:
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.high_score))
        except IOError:
            print("Saving failed...")

    def load_data(self):
        try:
            with open("data.txt", "r") as file:
                content = file.readlines()
                self.high_score = int(content[0])
        except (IOError, IndexError):
            print("File not found...\nInitializing data...")
