from turtle import  Turtle

# Creating Score traking class
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.right_paddle_score = 0
        self.left_paddle_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()


# Update score function
    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"{self.left_paddle_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(150, 200)
        self.write(f"{self.right_paddle_score}", align="center", font=("Arial", 50, "normal"))

    def left_score(self):
        self.left_paddle_score += 1
        self.update_score()

    def right_score(self):
        self.right_paddle_score += 1
        self.update_score()
