def print_stairs(n):
    for i in range(1, n + 1):
        print("#" * i)

number = int(input("Input number: "))
print_stairs(number)

# bai2
def input_positive_number():
    while True:
        number = float(input("Input a positive number: "))
        if number > 0:
            print("Thank you.")
            return
        else:
            print("Input a positive number:")

input_positive_number()

#bai3
def input_positive_number():
    while True:
        number = float(input("Input a positive number: "))
        if number > 0:
            print("Thank you.")
            return
        else:
            print("Input a positive number:")

input_positive_number()

#bai4
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

number = int(input("Input number: "))
print(f"Sum of digits of {number} = {sum_of_digits(number)}")

#bai5
def lucky_numbers():
    count = 0
    num = 1000
    while count < 10:
        if sum(int(digit) for digit in str(num)) == 9:
            print(num, end=" ")
            count += 1
        num += 1

print("Numbers with sum of digits = 9:")
lucky_numbers()

#bai6
import turtle

def draw_polygon(edges):
    angle = (edges - 2) * 180 / edges
    for _ in range(edges):
        turtle.forward(100)
        turtle.left(180 - angle)

edges = int(input("Input number of edges: "))
if edges > 2:
    draw_polygon(edges)
else:
    print("Invalid input")

turtle.done()

#bai7
import turtle

def draw_spiral():
    radius = 1
    while True:
        turtle.circle(radius, 180)
        radius += 1

draw_spiral()
turtle.done()
