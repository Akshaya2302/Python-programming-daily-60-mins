while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Thank you! Goodbye.")
            break

        if choice < 1 or choice > 5:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Answer:", a + b)
        elif choice == 2:
            print("Answer:", a - b)
        elif choice == 3:
            print("Answer:", a * b)
        elif choice == 4:
            print("Answer:", a / b)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter numbers only!")
