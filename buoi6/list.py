# colletion data types in python
# + List []: ordered , changeable, allows duplicate members
# + Tuple (): ordered, changeable, allows duplicate members
# + Set {}: unordered, unchangeable,unchangeable (add, remove items), no duplicate members
# + Dictionary {key: value}: ordered, changeable, no duplicate members.

# 1D List
food = ["bun bo", "ca chien", "xien ban", "tra sua"]
print(food)
print(type(food))
food[0] = "com tam "
print(food)

# foreach
for item in food:
    print(item)

# for
for ind in range(len(food)):
    print(ind, end=". ")
    print(food(ind))

# functions of list
    food.append("kem chuoi")
    food.remove("ca chien ")
    item = food.pop()
    print(item)
    print(food)
    food.insert(1, "banh da cua")
    food.sort()
    food.clear()
    print(item)
    print(food)

    # 2d list
    drinks = ["tra sua", "tra chanh", "nuoc ep"]
    dessert = ["banh plan", "kem"]

    meal = [food,drinks,dessert] #2d list
    print(meal[1][2])  # iteam trong 1 list nho
    print(meal[2]) # in dessert list

    #3 multable & immutable
    x = "abc" + "d"
    x = "abcd"

    # clone list
    list_clone = food.copy()
    # join 2 lists
    list1 = ["a", "b",7, True]
    list2 = [1,4,25.5]
    list3 = list1 + list2 #way1
    list4 = list1.extend(list2) #way2