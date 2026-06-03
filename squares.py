# Square of Numbers Program

count = int(input("Enter the number of values: "))

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    square = number * number
    print(f"Square of {number} = {square}")
