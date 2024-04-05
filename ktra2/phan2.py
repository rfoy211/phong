#p3
number_list = [5,1,8,92,-1,30]

search_number = int(input("Input a number:"))
if search_number in number_list:
    position = number_list.index(search_number) +1
    print(f"Number found at position{position}")
    print("Number not found")

sum_of_numbers = sum(number_list)
print(f"Sum of all numbers:{sum_of_numbers}")

user_numbers = []
while True:
    num = int(input("Enter a number(0 to finish):"))
    if num == 0:
        break
    user_numbers.append(num)

sum_of_user_numbers = sum(user_numbers)
print(f"Sum of numbers in list:{sum_of_user_numbers}")

user_numbers = []
while True:
    num = int(input("Enter a number(0 to finish):"))
    if num == 0:
        break
    user_numbers.append(num)

even_user_numbers = [num for num in user_numbers if num % 2 == 0]
print("Even numbers in list:",''.join(map(str,even_user_numbers)))