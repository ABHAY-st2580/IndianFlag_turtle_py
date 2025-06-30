import turtle

def rectangle(x,y,color,length,breadth):
    t = turtle.Turtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(breadth)
        t.left(90)
    t.end_fill()
    t.home()
    t.hideturtle()
    

def circle_(x,y,color,radius):
    t = turtle.Turtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.goto(x,y-radius)
    t.circle(radius)
    t.goto(x,y)
    t.color("blue")
    for i in range(24):
        t.forward(radius)
        t.backward(radius)
        t.left(15)
    t.up()
    t.home()
    t.hideturtle()

rectangle(0,100,"green",100,20)
rectangle(0,120,"white",100,20)
rectangle(0,140,"orange",100,20)
circle_(50,130,"blue",10)
turtle.done()