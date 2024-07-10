def reverse_(arr):
    arr = arr[::-1]
    return arr

def reverse(arr):
    left, right = 0, len(arr) - 1 
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


user_input = input("ENTER THE ATTAY ELEMENTS SEPARATED BY SPACE: ")
arr = list(map(int, user_input.split()))

reverse_array = reverse(arr)
print(*reverse_array)