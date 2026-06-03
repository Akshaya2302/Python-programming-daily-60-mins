def prime(n):
    if n<=1:
        return "Not Prime"
        
    for i in range(2,n):
        if n%i==0:
            return "Not Prime"
    return "Prime"

def even_odd(n):
    if n%2==0:
        return "Even"
    return "Oddd"

def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        
def fact(n):
    fact=1
    for i in range(1,n+1):

        fact=fact*i
        
    return fact
    


while True:
    print("\n 1.Prime 2,Even or Odd 3.Fibonacci series 4.Factorial 5.Exit")
    
    user_input=int(input("Enter Your Choice: "))
     
    if user_input==1:
        n = int(input("Enter a number: "))
        print(prime(n))
    elif user_input==2:
        n = int(input("Enter a number: "))
        print(even_odd(n))
    elif user_input==3:
        n = int(input("Enter the number of terms: "))
        fib(n)
    elif user_input==4:
        n = int(input("Enter a number: "))
        print(fact(n))
    elif user_input==5:
        break
    else:
        print("Invalid Choice")