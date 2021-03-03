from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 270)
        self.speed(0)
        self.write_score()

    def write_score(self):
        self.get_high_score()
        self.clear()
        self.write(arg=f"Score: {self.points} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.points += 1
        self.write_score()

    def reset(self):
        if self.points > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.points))
        self.get_high_score()
        self.points = 0
        self.write_score()

    def get_high_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
