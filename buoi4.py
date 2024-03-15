# print("your input: ", end="")
# name = input()

# def my_uppercase(str):
#     distance = ord('A') - ord('a')
#     for ch in str:
#         if ch > 'a' and ch < 'z':
#             print(chr(ord(ch)+ distance), end="")
#         else:
#             print(ch, end="")

# for
# import random
# my_list = ["apple", "orange", "banana"]

# random_list = random.choices(my_list, weights=[5,1,1], k=5)
# print(random_list)

# for ind, item in enumerate(random_list, start=1):
#     print(f"{ind}, {item}")

import turtle

num_sides = int(input("nhập số cạnh (> 2): "))

t = turtle.turtle()

for _ in range(num_sides):
    t.forward(100)
    t.left(360 / num_sides)

turtle.done()