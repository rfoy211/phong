# ktra hàm số chẵn
def is_even(number):
    return number % 2 == 0

# 2
def cal_area(radius) :
    return 3.14 * radius * radius

# 3
def reverse_str(text) :
    return text[:: -1]

# 4
def is_palindrome(text) :
    return text == text[:: -1]

number = int(input("input a number:"))
if is_even(number) :
    print("this number is even")
else:
    print("this number is not even:")

radius = float(input("input radius:"))
print("circle's area:", cal_area(radius))
text = input("input a text:")
print("reversed text:", reverse_str(text))

text_palindrome = input("input a text:")
if is_palindrome(text_palindrome) :
    print("this is a palidrome:")
else:
    print("this is not a palidrome")