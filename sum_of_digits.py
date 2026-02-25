digit = int(input("Enter the 2 digit number:"))

lastdigit = digit%10
firstdigit = digit//10
sum = firstdigit+lastdigit


print("Sum of 2 digits:",sum)