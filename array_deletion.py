def delete_element(arr, pos):
   
    for i in range(pos, len(arr) - 1):
        arr[i] = arr[i + 1]
    
    arr.pop()


user_input = input("ENTER THE ARRAY: ")
arr = list(map(int, user_input.split()))
pos = int(input("ENTER THE POSITION: ")) 

delete_element(arr, pos)
print("Array after deletion:", arr)
