def insert_element(arr, ele, pos):
    
    arr.append(0)
    for i in range(len(arr) - 1, pos, -1):
        arr[i] = arr[i - 1]
        
    arr[pos] = ele

user_input = input("ENTER THE ARRAY: ")
arr = list(map(int, user_input.split()))
ele = int(input("ENTER THE NEW ELEMENT: "))
pos = int(input("ENTER THE POSITION FOR THE NEW ELEMENT: "))

insert_element(arr, ele, pos)
print("Array after insertion:", arr)
