student = ("Phong", 25, "female", "Phong")

print(student.count("Phong")) # đếm số lần phần tử xuất hiện trng ds
print(student.index("female"))

for i in student:
    print(i)

if "Phong" in student:
    print("True")

# slicing
numbers = (22,3,4,5,67,89)
student[1:3]
student[:2]
student[:]
student[::5]
numbers[::3] #step
numbers[::-1] # dao nguoc danh sach
numbers[-4]
numbers[-4:-2]
