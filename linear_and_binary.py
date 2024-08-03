# Linear
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [3, 5, 2, 8, 6, 4, 3, 2, 1]
target = 8
result = linear_search(arr, target)
print(f"Element {target} indeks: {result}")


# Binary
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Element topildi va indeksi qaytarildi
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 6, 2, 90, ]
target = 9
result = binary_search(arr, target)
print(f"Element {target} indeksi: {result}")
