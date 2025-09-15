# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

