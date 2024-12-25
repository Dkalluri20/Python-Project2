import math


def display_menu():
    print("\n=== Simple Calculator ===")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    print("7. Floor Division (//)")
    print("8. Square Root")
    print("9. Logarithm")
    print("10. Trigonometric Functions (sin, cos, tan)")
    print("11. Exit")


def get_two_numbers():
    """Prompt the user for two numbers."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")


def get_one_number():
    """Prompt the user for one number."""
    while True:
        try:
            num = float(input("Enter the number: "))
            return num
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."


def modulus(a, b):
    return a % b


def exponentiation(a, b):
    return a ** b


def floor_division(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return "Error! Division by zero."


def square_root(a):
    if a < 0:
        return "Error! Cannot calculate the square root of a negative number."
    return math.sqrt(a)


def logarithm(a):
    if a <= 0:
        return "Error! Logarithm is undefined for zero or negative numbers."
    return math.log(a)


def trigonometric_function(func, angle):
    radians = math.radians(angle)
    if func == "sin":
        return math.sin(radians)
    elif func == "cos":
        return math.cos(radians)
    elif func == "tan":
        try:
            return math.tan(radians)
        except ValueError:
            return "Error! Tangent is undefined for this angle."


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-11): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 11.")
            continue

        if choice == 1:  # Addition
            num1, num2 = get_two_numbers()
            print(f"The result of addition: {addition(num1, num2)}")

        elif choice == 2:  # Subtraction
            num1, num2 = get_two_numbers()
            print(f"The result of subtraction: {subtraction(num1, num2)}")

        elif choice == 3:  # Multiplication
            num1, num2 = get_two_numbers()
            print(f"The result of multiplication: {multiplication(num1, num2)}")

        elif choice == 4:  # Division
            num1, num2 = get_two_numbers()
            print(f"The result of division: {division(num1, num2)}")

        elif choice == 5:  # Modulus
            num1, num2 = get_two_numbers()
            print(f"The result of modulus: {modulus(num1, num2)}")

        elif choice == 6:  # Exponentiation
            num1, num2 = get_two_numbers()
            print(f"The result of exponentiation: {exponentiation(num1, num2)}")

        elif choice == 7:  # Floor Division
            num1, num2 = get_two_numbers()
            print(f"The result of floor division: {floor_division(num1, num2)}")

        elif choice == 8:  # Square Root
            num = get_one_number()
            print(f"The square root of {num} is: {square_root(num)}")

        elif choice == 9:  # Logarithm
            num = get_one_number()
            print(f"The natural logarithm of {num} is: {logarithm(num)}")

        elif choice == 10:  # Trigonometric Functions
            print("\nChoose a trigonometric function:")
            print("a. Sine (sin)")
            print("b. Cosine (cos)")
            print("c. Tangent (tan)")
            trig_choice = input("Enter your choice (sin/cos/tan): ").lower()

            if trig_choice in ["sin", "cos", "tan"]:
                angle = float(input("Enter the angle in degrees: "))
                result = trigonometric_function(trig_choice, angle)
                print(f"The result of {trig_choice}({angle}°) is: {result}")
            else:
                print("Invalid choice! Please select sin, cos, or tan.")

        elif choice == 11:  # Exit
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid operation.")

        print("\n" + "=" * 30)  # Separator for readability


if __name__ == "__main__":
    main()
