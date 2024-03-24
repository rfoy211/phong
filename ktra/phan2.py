import turtle

# Hàm để in ra dãy số từ 3 đến 12
def day_so_tu_3_den_12():
    for num in range(3, 13):
        print(num, end=" ")
    print()

# Hàm để in ra dãy số từ 0 đến n
def day_so_tu_0_den_n():
    n = int(input("Nhập một số: "))
    for num in range(n + 1):
        print(num, end=" ")
    print()

# Hàm để in ra dãy số lẻ từ 0 đến n
def day_so_le_tu_0_den_n():
    n = int(input("Nhập một số: "))
    for num in range(1, n + 1, 2):
        print(num, end=" ")
    print()

# Hàm để vẽ một đa giác với số cạnh do người dùng nhập vào
def ve_da_giac_voi_so_canh_tu_chon():
    canh = int(input("Nhập số cạnh cho đa giác: "))
    goc = 360 / canh
    for _ in range(canh):
        turtle.forward(100)  
        turtle.right(goc)
    turtle.done()

# Hàm chính
def main():
    print("1. Dãy số từ 3 đến 12")
    day_so_tu_3_den_12()
    print("\n2. Dãy số từ 0 đến n")
    day_so_tu_0_den_n()
    print("\n3. Dãy số lẻ từ 0 đến n")
    day_so_le_tu_0_den_n()
    print("\n4.")
    ve_da_giac_voi_so_canh_tu_chon()

# Chạy hàm main
if __name__ == "__main__":
    main()
