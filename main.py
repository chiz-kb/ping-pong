from turtle import Screen, tracer
from paddle import Paddle
import time
from ball import Ball
from scorboard import Scoreboard

screen=Screen()

screen.setup(800,600)
screen.bgcolor('black')
screen.tracer(0)
r_paddle=Paddle(position=(350,0))
l_paddle=Paddle(position=(-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')
is_game_on=True
sleep_time=1
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380 : 
        ball.goto(0,0)
        ball.bounce_x()
        scoreboard.l_inc()
        ball.speed('fastest')
    if ball.xcor()<-380:
        ball.reset_po()
        scoreboard.r_inc()
        
    
        

screen.exitonclick()