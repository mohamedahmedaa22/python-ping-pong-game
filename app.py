#import turtle module

import turtle

wind = turtle.Screen()
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)

wind.tracer(0) # stop update the screen


#player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

#player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

#functions
def player1_move_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_move_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_move_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_move_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

#keybord bindings
wind.listen()
wind.onkeypress(player1_move_up, 'w')
wind.onkeypress(player1_move_down, 's')
wind.onkeypress(player2_move_up, 'Up')
wind.onkeypress(player2_move_down, 'Down')

while True:
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1