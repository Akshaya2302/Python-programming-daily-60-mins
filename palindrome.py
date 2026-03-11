def palindrome():
    reversed_number = 0

    num = int(input("Enter the number:"))
    original_num = num
    while num>0:
        dig = num%10
        reversed_number = (reversed_number*10)+dig
        num = num//10
       
    if original_num == reversed_number:
            print("The given number is a palindrome..")
    else :
            print("Its not a palindrome") 
palindrome()
    