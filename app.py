#import turtle module

import turtle

wind = turtle.Screen()
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)

wind.tracer(0) # stop update the screen

while True:
    wind.update()