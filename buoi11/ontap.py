# lambda
def sum(x,y):
    return x + y

sum_lambda = lambda x, y: x + y
print(sum_lambda(10, 2))

#sort, map, filter
students = (
    ("A", 12),
    ("E", 15),
    ("B", 13),
    ("D", 14),
    ("C", 11),
    ("F", 16),
)
students_name = ["A", "B", "C", "D", "E", "F"]
sorted_students = sorted(students)
print(sorted_students)

students_name = ["A", "B", "C", "D", "E", "F"]
students_name.sort()
students_name.sort(reverse=True)
print(students_name)

age = lambda item: item[1]
sorted_ages = sorted(students, key=age)
print(sorted_ages)

# map() = applies a function to each item in an iterable
store_dollars = [("apple", 1),("jacket", 50), ("paints", 40),("skirt", 80)]
store_euros = list(map((lambda item: (item[0], item[1 * 0.82])), store_dollars))
print(store_euros)

#filter() = creates a collection of elements from an iterable for which a func returns
filter_students = tuple(filter((lambda item: item[1] >= 14),students))
print(filter_students)

# list/ dictionary comprehension
cols = 5
rows = 3
new_map = []
for i in range(cols):
    col = []
    for j in range(cols):
        col.append('-')
    new_map.append(col)
print(new_map)

# way 2
new_map_2 = [['-']*cols for i in range(rows)]
print(new_map_2)

# dictionary = {key: expression for (key,value) in iterable}
cities_in_F = {"new york": 32, "boston": 75, "los angles": 100, "chicago": 50}
cities_in_C =  {
    key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()
}

# TH2
print("TRUE") if 10 % 2 == 0 else print("FALSE")
odd_list = [item for item in range(1, 11) if item % 2 == 0]
print(odd_list)

# dictionary = {key: expression for (key, value)in iterable if conditional}
warn_cities = {key: value for (key, value)in cities_in_F.items()if value > 40}
print(warn_cities)

# TH3
students = [50, 40, 70, 80, 100, 0]
passed_list = list(filter(lambda sc: sc >= 60, students))
new_class = [item if item >= 60 else "FALSE" for item in students]

cities_status = {
    key: "WARM" if value > 40 else "COLD" for (key, value) in cities_in_F.items()
}
print(cities_status)

#TH4
def check_temp(value):
    if value > 60:
        return "HOT"
    elif 40 <= value < 60:
        return "WARM"
    else:
        return "COLD"
    
cities_weather = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(cities_weather)