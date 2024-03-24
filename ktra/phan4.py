import re

# Hàm đăng ký tài khoản
def registration():
    print("== Registration ==")
    username = input("Username: ")
    password = input("Password: ")
    repeat_password = input("Repeat password: ")
    while password != repeat_password:
        print("Passwords not match. Please input again.")
        repeat_password = input("Repeat password: ")
    email = input("Email: ")
    while not is_valid_email(email):
        print("Invalid email. Please input again.")
        email = input("Email: ")
    while not is_valid_password(password):
        print("Invalid password. Please input again.")
        password = input("Password: ")
        repeat_password = input("Repeat password: ")
        while password != repeat_password:
            print("Passwords not match. Please input again.")
            repeat_password = input("Repeat password: ")
    print("Registered successfully.")

# Hàm kiểm tra email hợp lệ
def is_valid_email(email):
    pattern = r''
    return re.match(pattern, email)

# Hàm kiểm tra mật khẩu hợp lệ
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search("[phong2001]", password):
        return False
    if not re.search("[2001]", password):
        return False
    return True

# Hàm chính
def main():
    registration()

# Chạy hàm main
if __name__ == "__main__":
    main()
