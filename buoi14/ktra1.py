# # bai1
# num1 = int(input("input first number: "))
# num2 = int(input("input second number: "))

# total = num1 + num2
# print(f"{num1} + {num2} = {total}")

#bai2
# a = float(input("input a: "))
# b = float(input("input b: "))
# c = float(input("input c: "))

# delta = b**2 - 4*a*c
# if delta > 0:
#     x1 = (-b + math.sqrt(delta)) / (2*a)
#     x2 = (-b - math.sqrt(delta)) / (2*a)
#     print(" the equation has 2 solutions.")
#     print(f"x = {x1} or x = {x2}")
# elif delta == 0:
#     x = -b / (2*a)
#     print("the equation has 1 solution.")
#     print(f"x = {x}")
# else:
#     print("the equation has no real solutions.")

# bai3
# def is_palindrome(s):
#     return s == s[::-1]

# text = input("input a text: ")
# if is_palindrome(text):
#     print("this is a palindrome.")
# else:
#     print("this is not a palindrome.")

# bai4
# print("==welcome to r-foy restaurant==")
# ordered_dishes = []

# while True:
#     dis = input("please choose a dish: ")
#     if dish not in ordered_dishes:
#         ordered_dishes.append(dish)
#         print("great choice! ", end='')
#     else:
#         print("you chose this already. " end='')

#     another = input("anything else? (y/n): ")
#     if another.lower() != 'y':
#         break

# print("well done! your order: ")
# for dish in ordered_dishes:
#     print(f"- {dish}")

# bai5
# phone_prices = {
#     "iphone12": 28000000,
#     "samsung N10": 16000000,
#     "oppo 93": 7500000,
#     "vsmart": 7400000,
#     "vivo": 4200000
# }

# phone_name = input("input name of a phone: ")
# if phone_name in phone_prices:
#     print(f"price of {phone_name} : {phone_prices[phone_name]}")
# else:
#     print(f"sorry, we don't have price information for {print}.")

# budget = int(input("input your budget: "))
# print("phone that fit your budget: ")
# for phone, price in phone_prices.items():
#     if price <= budget:
#         print(f"- {phone}: {price}")

# bai6
# number = int(input("input  number: "))
# if number > 0:
#     num_digits = len(str(number))
#     print(f"this number has {num_digits} digit(s).")
# else:
#     print("please enter a positive integer: ")

# bai7
# numbers = [5, 1, 8, 92, -1, 30]
# print("original list: ")
# print(" ".join(map(str, numbers)))

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr [j], arr[j+1] = arr[j+1], arr[j]

# bubble_sort(numbers)
# print("sorted list: ")
# print(" ".join(map(str, numbers)))

#bai8
n = int(input("input a number: "))
if n > 0:
    def fibonacci(n):
        fib_sequence = [1, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[:n]
    
    fib_numbers = fibonacci(n)
    print(f"firts {n} fibonacci number: {' '.join(map(str, fib_numbers))}")
else:
    print("please enter a positive integer.")