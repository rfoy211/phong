def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

number = int(input("Input number: "))
check_even_odd(number)

#bai2
def check_integer(num):
    if num == int(num):
        print(f"{num} is an integer")
    else:
        print(f"{num} is not an integer")

number = float(input("Input number: "))
check_integer(number)

#bai3
def check_digit(character):
    if character.isdigit():
        print(f"'{character}' is a digit")
    else:
        print(f"'{character}' is not a digit")

character = input("Input character: ")
check_digit(character)

#bai4
def check_divisibility(n):
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} is divisible by 3 and 5")
    elif n % 3 == 0:
        print(f"{n} is divisible by 3")
    elif n % 5 == 0:
        print(f"{n} is divisible by 5")
    else:
        print(f"{n} is not divisible by 3 or 5")

number = int(input("Input number: "))
check_divisibility(number)

#bai5
def login(username, password):
    if username == "admin" and password == "12345":
        print("You are logged in, admin.")
    else:
        print("Wrong username or password.")

print("Welcome to The Ultimate Security System")
username = input("Username: ")
password = input("Password: ")
login(username, password)

#bai6
def check_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("The 3 line segments can form a triangle.")
    else:
        print("The 3 line segments cannot form a triangle.")

a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))
check_triangle(a, b, c)

#bai7
import math
import turtle

def check_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("The 3 line segments can form a triangle.")
        if a == b == c:
            print("The triangle is equilateral.")
            turtle.forward(a)
            turtle.left(120)
            turtle.forward(b)
            turtle.left(120)
            turtle.forward(c)
        elif a == math.sqrt(b**2 + c**2) or b == math.sqrt(a**2 + c**2) or c == math.sqrt(a**2 + b**2):
            print("The triangle is right.")
        else:
            print("The triangle is normal.")
    else:
        print("The 3 line segments cannot form a triangle.")

a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))
check_triangle(a, b, c)

turtle.done()
