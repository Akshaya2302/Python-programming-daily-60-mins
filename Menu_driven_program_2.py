def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_even_odd(n):
    """Returns 'Even' if the number is even, otherwise 'Odd'."""
    if n % 2 == 0:
        return "Even"
    return "Odd"


def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        return "Error! Factorial is not defined for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def generate_fibonacci(n):
    """Generates Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series


def main_menu():
    """Displays the menu and handles user choices."""
    while True:
        print("\n" + "=" * 30)
        print("          MAIN MENU          ")
        print("=" * 30)
        print("1. Check Prime Number")
        print("2. Check Even or Odd")
        print("3. Find Factorial")
        print("4. Generate Fibonacci Series")
        print("5. Exit")
        print("=" * 30)

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            print("Exiting the program. Goodbye!")
            break

        # Menu choices that require a single integer input
        if choice in [1, 2, 3, 4]:
            try:
                num = int(input("Enter the number: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue

            if choice == 1:
                if is_prime(num):
                    print(f"👉 {num} is a Prime number.")
                else:
                    print(f"👉 {num} is NOT a Prime number.")

            elif choice == 2:
                result = check_even_odd(num)
                print(f"👉 {num} is an {result} number.")

            elif choice == 3:
                result = factorial(num)
                print(f"👉 The factorial of {num} is: {result}")

            elif choice == 4:
                result = generate_fibonacci(num)
                print(f"👉 Fibonacci series up to {num} terms: {result}")

        else:
            print("Invalid choice! Please select an option from 1 to 5.")


# Run the program
if __name__ == "__main__":
    main_menu()
