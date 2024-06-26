def insert_element(arr, ele, pos):
    # Ensure position is within bounds
    if pos < 0 or pos > len(arr):
        print("INVALID POSITION")
        return arr
    
    # Extend the array by one element
    arr.append(None)

    # Shift elements to the right from end to position
    for i in range(len(arr)-1, pos, -1):
        arr[i] = arr[i-1]

    # Insert the new element at the specified position
    arr[pos] = ele
    
    return arr

user_input = input("Enter the array elements separated by space: ")
arr = list(map(int, user_input.split()))

ele = int(input("Enter the element to inserted: "))
pos = int(input("Enter the postion to insert the element: "))

# Using in-built function:
# arr.insert(pos, ele)
# Displaying the updated array
# print("Updated array:", arr)

updated_arr = insert_element(arr, ele, pos)
print(updated_arr)