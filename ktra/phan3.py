# Hàm kiểm tra số lớn hơn 13
def lon_hon_13():
    number = float(input("Nhập một số: "))
    if number > 13:
        print("Số này lớn hơn 13")
    else:
        print("Số này không lớn hơn 13")

# Hàm kiểm tra số chẵn
def kiem_tra_so_chan():
    number = int(input("Nhập một số: "))
    if number % 2 == 0:
        print("Số này là số chẵn")
    else:
        print("Số này không là số chẵn")

# Hàm để in ra số ngày của tháng
def so_ngay_cua_thang():
    month = int(input("Nhập một tháng trong năm: "))
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("Tháng này có 31 ngày")
    elif month in [4, 6, 9, 11]:
        print("Tháng này có 30 ngày")
    elif month == 2:
        print("Tháng này có 28 hoặc 29 ngày")

# Hàm chính
def main():
    print("1. Kiểm tra số lớn hơn 13")
    lon_hon_13()
    print("\n2. Kiểm tra số chẵn")
    kiem_tra_so_chan()
    print("\n3. Số ngày của tháng")
    so_ngay_cua_thang()

# Chạy hàm main
if __name__ == "__main__":
    main()
