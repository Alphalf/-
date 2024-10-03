import turtle
t=turtle.Pen()
turtle.bgcolor("white")
colors=["red","green","blue","yellow"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
