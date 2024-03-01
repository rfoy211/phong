# print string has multi lines
S = "There are\multi\nlines"
print(S)

S1 = """This is
    multi
lines"""
print(S1)
# operator fot str 
# x = input("type a number: ")
# print("you have "+ x +" son")
# print(f"you have {x} son")

# a = "abc"
# print(a*5)

# string methods
name = input("Your name: ")
# print(len(name))
# print(name.find("D"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.count("d"))
# print(name.replace("d", "b"))
# print(name.isalpha())

# slicing = create a subtring by extracting elements from another string
# name = "Phong"
# first_name = name[name.find("P"):3]
# first_name = name[:3]
# print(first_name)

# last_name = name[name.find("G"):]
# print(last_name)
# reserve_name = name[::-1]
# print(reserve_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice_web_name = slice(7, -4)
slice_web_name = slice(7, website1.find("."))
web1_name = website2[slice_web_name]
print(web1_name)

# type casting = convert the data type of a value to another 