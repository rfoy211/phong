# Bài 1: Số Nguyên
def is_int(num):
    return isinstance(num, int)

number = float(input("Input number: "))
if is_int(number):
    print(f'{int(number)} is an integer')
else:
    print(f'{number} is not an integer')

# Bài 2: Số Nguyên Tố
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Input number: "))
if is_prime(number):
    print(f'{number} is a prime')
else:
    print(f'{number} is not a prime')

# Bài 3: Liệt Kê Số Nguyên Tố
def list_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Input number: "))
primes = list_primes(n)
print(f"First {n} prime(s): {' '.join(map(str, primes))}")

# Bài 4: Biểu Thức Đặc Biệt
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def special_expression(n):
    result = 0
    for i in range(1, n + 1):
        result += factorial(i)
    return result

n = int(input("Input number: "))
print("Result:", special_expression(n))

# Bài 5: Datetime
from datetime import datetime

now = datetime.now()
print(f"Today is {now.strftime('%d/%m/%Y')}")
print(f"Time right now: {now.strftime('%H:%M:%S')}")
