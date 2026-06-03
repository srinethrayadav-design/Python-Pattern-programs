# Diamond  Pattern

n = int(input("Enter number of rows: "))

# Upper Part
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()

# Lower Part
for row in range(n - 1, 0, -1):
    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
