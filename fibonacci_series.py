n = int(input("Enter the positive Integer:"))
a=0
b=1
if n<=0:
    print("Please! Enter a number greater than Zero!!!")
else:
    for _ in range(n):
        a, b = b, a+b
        print(a, end=" ")