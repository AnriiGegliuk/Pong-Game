from turtle import Turtle

# Creating Ball class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor_move = 10
        self.y_cor_move = 10
        self.move_ball_speed = 0.1

# Function to move ball
    def move(self):
        new_x = self.xcor() + self.x_cor_move
        new_y = self.ycor() + self.y_cor_move
        self.goto(new_x, new_y)

    def bounce_ycor(self):
        self.y_cor_move *= -1

    def bounce_xcor(self):
        self.x_cor_move *= -1
        self.move_ball_speed *= (0.9)

# Function to start new game when point is missed by any side
    def start_new_game(self):
        self.goto(0, 0)
        self.move_ball_speed = 0.1
        self.bounce_xcor()
