num_of_item = int(input("Number of item in menu: "))
menu = []
for i in range(num_of_item):
    name = (input(f"Name of item {i} : "))
    price = float(input(f"Price of item {i} : "))
    menu.append((name, price))
def avgPrice(arr):
    my_sum = 0
    for i in arr:
        my_sum += i[1]
    return round((my_sum / num_of_item) * 100) / 100
avg = avgPrice(menu)
print("Average price:", avg)
result = "Item(s) above average price: "
for i in menu:
    if i[1] > avg:
        result += str(i) + ", "

print(result)