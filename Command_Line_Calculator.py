# COMMAND LINE CALCULATOR

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Enter 'exit' to quit.")
        num1 = input("Enter the first number: ")
        if num1.lower() == 'exit':
            print("Goodbye!")
            break

        num2 = input("Enter the second number: ")
        operator = input("Enter an operator (+, -, *, /): ")

        try:
            num1, num2 = float(num1), float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed!")
                    continue
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

calculator()