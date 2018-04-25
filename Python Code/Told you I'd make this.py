import turtle
def writing():
    turtle.penup()
    turtle.colormode(255)
    turtle.color(0,255,0)
    turtle.goto(30,-30)
    turtle.pendown()
    turtle.write("Bitcoin be like", False, align="center", font=("Arial", 16, "normal"))
    turtle.penup()

def graph():
    turtle.color(0,0,0)
    turtle.goto(0,0)
    turtle.pendown()
    turtle.forward(400)
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(400)
    turtle.goto(0,0)
    turtle.color(49,233,22)
    turtle.speed(1)
    turtle.right(45)
    turtle.forward(60)
    turtle.left(20)
    turtle.forward(400)
    turtle.right(130)
    turtle.color(255,0,0)
    turtle.right(10)
    turtle.forward(200)
    turtle.right(15)
    turtle.speed(5)
    turtle.forward(700)
writing()
graph()

leave = input("Enter to exit.")




