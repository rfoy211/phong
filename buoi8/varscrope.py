x = 12 # global var

def my_func ():
    global x
    x = 10 # local var
print(x)
my_func()
print(x)

if 3 < 4:
    a = 10
else:
    print(1)

# print(a)
# print(x)

# def square (w, h):
#     global s
#     s = w * h

# # square()
# square(4,3)
# print(s)
