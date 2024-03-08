# # age
# age = input("Enter your age: ")

# if (age < 0):
#     print("not born")
# elif (age < 18):
#     print("teen")
# elif (age < 60):
#     print("adult")
# else:
#     print("old")

# # boolean
# a = True
# b = False

# print(a and b )
# print(b or a )
# print ( not a)
# print (not b)

# keo bua bao
# import random
# list_str = ["keo", "bua" , "bao"]

# def randomSkill(list_skill):
    
#     return random.choice(list_skill)
# userInput = input("keo, bua or bao? ")

# machineInput = randomSkill(list_str)
# def checkResult(user, machine):
#     if (user == "keo"):
#         if (machine == "bao"):
#             print("thang")
#         elif(machine == "bua"):
#             print("thua")
#         else:
#             print("hoa")

#     if (user == "bao"):
#         if (machine == "keo"):
#             print("thang")
#         elif(machine == "bua"):
#             print("thua")
#         else:
#             print("hoa")

#     if (user == "bua"):
#         if (machine == "bao"):
#             print("thang")
#         elif(machine == "keo"):
#             print("thua")
#         else:
#             print("hoa")
# print(machineInput)
# checkResult(machine=machineInput, user=userInput)

# user_input = None
# while(not user_input):
#     user_Input = input("ok")
#     if (user_input == "y"):
#         break
#     else:
#         user_input = None
#         continue

# for
# range
# arr = range(1, 10, 3)
# for i in arr:
#     print(i)

# import time

# for i in "Happy New Year":
#     print(i)
#     time.sleep(1) # wait 1 sec
# print("Happy New Year")

user_input = None
while(not user_input):
    user_input = input("2 , 4 ,6 ,8 ,10")
    if (user_input == "2"):
        break
    else:
        user_input = None
        continue