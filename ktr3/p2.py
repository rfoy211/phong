def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def sort_list(lst):
    for i in range(len(lst)) :
        for j in range(i+1, len(lst)) :
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

def print_fibo(n) :
    fibo_list = [1, 1 ]
    for i in range(2, n):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    print("first", n, "fibonacci number:", ' ' .join(map(str, fibo_list)))

number = int(input("input a number;"))
print(f"{number}! =", factorial(number))
num_list = [5, 1, 8, 92, -1, 30]
print("original list:")
print(' '.join(map(str, num_list)))
sort_list(num_list)
print("sorted list:")
print(' '.join(map(str, num_list)))

n = int(input("input a number:"))
print_fibo(n)