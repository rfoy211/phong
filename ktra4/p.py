#Phần1
computers = {
  "HP": 20,
  "DELL": 5,
  "MACBOOK": 12,
  "ASUS": 30
 }

print("available MACBOOKs", computers["MACBOOK"])
brand_input = input("input a brand: ")

if brand_input in computers:
    print("available", brand_input, ":" , computers[brand_input])
else:
    print("brand not found! ")
#Phần2
computers["TOSHIBA"] = 10
print("availabble products: ")
for brand, quantity in computers.items():
    print("-", brand + ":" , quantity)

brand_input = input("input a brand: ")
amount_input = int(input("input amount: "))

computers[brand_input] = amount_input
print("available products: ")

computers["DELL"] += 10
computers["MACBOOK"] -= 2
print("available products: ")
for brand, quantity in computers.items():
    print("-", brand + ":", quantity)

total_products = sum(computers.values())
print("total products: ", total_products)
#Phan3
prices ={
    "HP": 60,
    "DELL": 65,
    "MACBOOK": 120,
    "ASUS": 200,
}
print("prices of ASUS: ",prices["ASUS"])
brand_input = input("input a brand: ")
print("prices of", brand_input + ":", prices[brand_input])

#Phần4
order_brand = "ASUS"
order_quantity = 10
total_prices = prices[order_brand] * order_quantity
print("total price: ", total_prices)

brand_input = input("input a brand: ")
amount_input = int(input("input a brand: "))

print("available products: ")
for brand, quantity in computers.items():
    print("-", brand + ":", quantity)

#Phan5
print("total value of available barand: ")
for brand, quantity in computers.items():
    total_value = quantity * prices[brand]
    print("-", brand + ":", total_value)

total_value_all_items = sum(quantity * prices[brand] for brand, quantity in computers.items())
print("total value of avaulable items: ", total_value_all_items)