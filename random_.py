import random
num = random.randint(1,100)
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    elif guess == num:
        print("Correct!")
        break   