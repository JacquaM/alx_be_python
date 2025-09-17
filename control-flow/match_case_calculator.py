import sys

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        if sys.version_info >= (3, 10):
            # Use real match-case syntax inside a string so it won't cause SyntaxError in Python < 3.10
            code = f'''
match "{operation}":
    case "+":
        print("The result is", {num1} + {num2})
    case "-":
        print("The result is", {num1} - {num2})
    case "*":
        print("The result is", {num1} * {num2})
    case "/":
        if {num2} == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is", {num1} / {num2})
    case _:
        print("Invalid operation.")
'''
            exec(code)  # Only runs if Python 3.10+, so no syntax error on 3.8
        else:
            # Fallback for Python 3.8 and earlier
            if operation == '+':
                print("The result is", num1 + num2)
            elif operation == '-':
                print("The result is", num1 - num2)
            elif operation == '*':
                print("The result is", num1 * num2)
            elif operation == '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("The result is", num1 / num2)
            else:
                print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()

