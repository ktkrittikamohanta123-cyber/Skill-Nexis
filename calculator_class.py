# Calculator Class with Exception Handling
# Supports addition, subtraction, multiplication, and division

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2


# Main program
calculator = Calculator()

while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select 1 to 5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = calculator.add(num1, num2)
        elif choice == "2":
            result = calculator.subtract(num1, num2)
        elif choice == "3":
            result = calculator.multiply(num1, num2)
        else:
            result = calculator.divide(num1, num2)

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as error:
        print("Error:", error)
