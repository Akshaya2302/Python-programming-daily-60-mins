while True:
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Answer:", result)

    except ValueError:
        print("❌ Enter numbers only!")

    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")

    again = input("Try again? (yes/no): ")
    if again != "yes":
        print("Goodbye!")
        break