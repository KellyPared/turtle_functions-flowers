#Rainbow Challenge - www.101computing.net/rainbow-challenge
import turtle
import random
import math

bob  = turtle.Turtle()
bob.shape("turtle")
bob.speed(500)

window = turtle.Screen()
window.bgcolor("#69C5FF")

rainbowColors = ['#FF1493', "#34ebe8","#34ebe8", "#FF0000","#FFA600","#FFC0CB", "#62FF00", "#1E56FC","#4800FF","#CC00FF", ]
#color = random.choice(rainbowColors)
#size=50
bob.penup()
#bob.goto(0,0)

location = bob.goto(random.randint(-300, 300), random.randint(-300, 300))
def flower(color, location):
    location = bob.goto(random.randint(-300, 300), random.randint(-300, 300))
    size = random.randint(20,35)
    for i in range(8):
      bob.color(color)
      bob.fillcolor(color)
      bob.begin_fill()
      bob.circle(size)
      bob.end_fill()
      bob.right(60)
    center = location
    #bob.goto
    #bob.goto(center)
    bob.color("yellow")
    bob.begin_fill()
    bob.circle(size/2)
    bob.end_fill()



while True:
    color = random.choice(rainbowColors)
    #center = location
    #center = bob.goto((location) *2 *math.pi)
    flower(color, location)
