def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for a in range(0, n-i-1):
            if arr[a] > arr[a+1]:
                            arr[a], arr[a+1] = arr[a+1], arr[a]

arr = [68,38,23,12,11,90]
print("sắp xếp DS", arr)
bubble_sort(arr)
print("sắp xếp DS", arr)