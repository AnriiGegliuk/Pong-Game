from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Screen parameters
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Calling paddle and ball classes
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# Calling onkey functions
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# When screen.tracer(0) screen needs to be updated & move ball function
game_is_on = True
while game_is_on:
    time.sleep(ball.move_ball_speed)
    screen.update()
    ball.move()

# Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ycor()

# Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_xcor()


# Detecting when each side missed a ball
    if ball.xcor() > 380:
        ball.start_new_game()
        score.left_score()

    if ball.xcor() < -380:
        ball.start_new_game()
        score.right_score()

screen.exitonclick()