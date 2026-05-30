"""
Menu-Driven Calculator with Exception Handling
Performs: Addition, Subtraction, Multiplication, Division
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def get_number(prompt):
    """Prompt the user and return a valid float. Raises ValueError on bad input."""
    value = input(prompt).strip()
    return float(value)   # raises ValueError if not numeric


def display_menu():
    """Print the operation menu."""
    print("\n" + "=" * 40)
    print("        MENU-DRIVEN CALCULATOR")
    print("=" * 40)
    print("  1. Addition       ( + )")
    print("  2. Subtraction    ( - )")
    print("  3. Multiplication ( * )")
    print("  4. Division       ( / )")
    print("  5. Exit")
    print("=" * 40)


def main():
    print("\nWelcome to the Menu-Driven Calculator!")

    while True:
        display_menu()

        # ── Validate menu choice ──────────────────────────────────────────────
        try:
            choice = int(input("Enter your choice (1-5): ").strip())
        except ValueError:
            print("\n[ERROR] Invalid choice! Please enter a number between 1 and 5.")
            continue

        # ── Exit condition ────────────────────────────────────────────────────
        if choice == 5:
            print("\nThank you for using the Calculator. Goodbye!\n")
            break

        if choice not in (1, 2, 3, 4):
            print("\n[ERROR] Invalid option! Please select a number from 1 to 5.")
            continue

        # ── Get numeric operands ──────────────────────────────────────────────
        try:
            num1 = get_number("Enter the first  number : ")
            num2 = get_number("Enter the second number : ")
        except ValueError:
            print("\n[ERROR] Invalid input! Please enter numeric values only.")
            continue

        # ── Perform the selected operation ────────────────────────────────────
        try:
            if choice == 1:
                result = add(num1, num2)
                operator = "+"
            elif choice == 2:
                result = subtract(num1, num2)
                operator = "-"
            elif choice == 3:
                result = multiply(num1, num2)
                operator = "*"
            elif choice == 4:
                result = divide(num1, num2)
                operator = "/"

            # ── Display result ────────────────────────────────────────────────
            print(f"\n  Result : {num1} {operator} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"\n[ERROR] {e}")

        except Exception as e:
            print(f"\n[ERROR] An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()