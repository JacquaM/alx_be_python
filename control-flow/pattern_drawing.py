# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after printing each row
    row += 1

