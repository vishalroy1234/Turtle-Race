
from turtle import Turtle, Screen
import random
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -100

bet_turtle = screen.textinput(title="Bet your winner?", prompt="Enter the color of the turtle which will win:")

for _ in range(6):
    tim = Turtle("turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(x=-450, y=y)
    turtles.append(tim)
    y += 50

speeds = [1, 2, 3, 4, 5, 6]
while True:
    turtles[0].forward(random.choice(speeds))
    turtles[1].forward(random.choice(speeds))
    turtles[2].forward(random.choice(speeds))
    turtles[3].forward(random.choice(speeds))
    turtles[4].forward(random.choice(speeds))
    turtles[5].forward(random.choice(speeds))
    if turtles[0].xcor() >= 450.0 or turtles[1].xcor() >= 450.0 or turtles[2].xcor() >= 450.0 or \
       turtles[3].xcor() >= 450.0 or turtles[4].xcor() >= 450.0 or turtles[5].xcor() >= 450.0:
        break

winner = Turtle()
max_x = 0.0
for turtle in turtles:
    if turtle.xcor() >= max_x:
        winner = turtle
        max_x = turtle.xcor()

if bet_turtle == winner.color()[0]:
    print("You win")
else:
    print("You lose")
print(f"The winner is the {winner.color()[0]} turtle")

for turtle in turtles:
    print(f"{turtle.color()}: {turtle.xcor()}")

screen.screensize(canvheight=400, canvwidth=500)
screen.exitonclick()


