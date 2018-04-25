from random import randint
import sys
import turtle

print("Welcome to random number generator v2!")
print("\nThis new version allows you to choose how big the maximum number will be.")
print("\nAlso, it has a secret feature that consists of an option.If you know me, you'll figure it out.")
print("Or you can look in the code and be a cheater.")
size=int(input("\nPlease enter how big the number shall be:\n"))
x=int(input("\nPlease enter how many random numbers you wish for:\n"))

if size == 21 and x == 69:
    print("Good shit fam...")
    print("Here, have some turtle drawing.")
    turtle.colormode(255)
    turtle.color(102,0,204)
    turtle.write("YA DON IT!", move=True, align="center", font=("Arial", 50, "normal"))
    
    
    secret=input("Press enter to fucking quit. Good job, if you did it legit that is.")
    
for i in range(x):
    print(randint(0, size))


leave=input("Press enter to leave.")
