n = int(input("Enter the number: "))

# Generate the increasing pattern
for i in range(1, n + 1):
    print('1' * i)

# Generate the decreasing pattern
for i in range(n - 1, 0, -1):
    print('1' * i)
