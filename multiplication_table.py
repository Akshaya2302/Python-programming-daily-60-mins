
num = int(input("Enter a number to see its multiplication table: "))

print(f"--- Multiplication Table for {num} ---")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")