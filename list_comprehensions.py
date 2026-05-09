numbers = [1, 2, 3, 4, 5, 6]
squared_evens = []

for n in numbers:
    if n % 2 == 0:
        squared_evens.append(n ** 2)

print(squared_evens)  # Output: [4, 16, 36]
