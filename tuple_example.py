
my_tuple = ("apple", "banana", "cherry")
print(f"Original Tuple: {my_tuple}")
print(f"First item: {my_tuple[0]}")
print(f"Last item: {my_tuple[-1]}")

fruits = ("apple", "mango", "papaya")
(green, yellow, orange) = fruits

print("\nUnpacked values:")
print(f"green: {green}")
print(f"yellow: {yellow}")
print(f"orange: {orange}")

numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

fives_count = numbers.count(5)
print(f"\nNumber of 5s in the tuple: {fives_count}")

index_of_eight = numbers.index(8)
print(f"The first index of 8 is: {index_of_eight}")
