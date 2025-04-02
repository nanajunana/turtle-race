from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coordinates = [125, 75, 25, -25, -75, -125]
turtle_list = []
is_race_on = False
winner = None

for _ in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[_])
    new_turtle.goto(x=-230, y=y_coordinates[_])
    turtle_list.append(new_turtle)

user_input = screen.textinput(title="Who's gonna win?", prompt="Pick your turtle!")
if user_input:
    is_race_on = True

while is_race_on and user_input:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 11))
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            break

if user_input == winner:
    print(f"You win! {winner} wins")
else:
    print(f"You lose! {winner} wins")


screen.exitonclick()
