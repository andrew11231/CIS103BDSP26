#Andrew Espinoza
import turtle
t = turtle.Turtle()SS
screen = turtle.Screen()
screen.title('Turtl Program')


t.pencolor('lightgreen')
t.penup()
t.goto(0,-300)
t.pensize(5)
t.pendown()
t.circle(300)

t.pencolor('red')
t.penup()
t.goto(-130,50)
t.pensize(2)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(80)
t.end_fill()


t.pencolor('blue')
t.penup()
t.goto(130,50)
t.pensize(2)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.circle(80)
t.end_fill()

t.pencolor('yellow')
t.penup()
t.goto(-140,-40)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
for i in range(2):
    t.forward(260)
    t.right(90)
    t.forward(30)
    t.right(90)

t.end_fill()

t.penup()
t.goto(-80,-240)
t.pencolor('black')
t.pensize(30)
t.pendown()
for i in range(3):
    t.forward(170)
    t.right(120)
            








