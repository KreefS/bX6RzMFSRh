import turtle

def hexagon(length):
    for i in range(6):
        turtle.forward(length)
        turtle.left(60)

def shape(shapeSide,long):  #You can add your own parameters
    for d in range(shapeSide):  #And also use the turtle.right and left but I don't know how yet.
        turtle.forward(long)
        turtle.left(360 / shapeSide)


def move():
    direction= input("Where to go? Left or right?")
    direction=direction.strip().lower() #This is data munging which basically
    if direction == "left":             #turns the input into a basic non-capital, no white space string so
        turtle.left(180)                #you can more easily check for the right input.
        turtle.forward(100)
    if direction == "right":
        turtle.forward(100)


while turtle.distance(0,0) <100:
    turtle.forward(5)
    if turtle.distance(0,0) >= 99:
        turtle.setheading(turtle.towards(0,0))
        turtle.forward(1)


def spiral(length):
    while 1== 1:
        length = length + 5
        turtle.forward(length)
        turtle.left(30)
        if turtle.xcor() and turtle.ycor() >=10000:
            break

def box():
    while 1==1:
        turtle.forward(2)
        if turtle.distance(0,0) >= 100:
            turtle.setheading(turtle.towards(0,0))





leave=input("Enter to leave\n")