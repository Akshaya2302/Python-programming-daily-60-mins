# --- Lists ---
# Lists are ordered, changeable (mutable), and allow duplicate values.
print("--- LISTS ---")
my_list = ["apple", "banana", "cherry"]
print(f"Original list: {my_list}")

# Modifying a list
my_list[1] = "blueberry"
my_list.append("orange")
print(f"Modified list: {my_list}")

# Removing an item
my_list.remove("apple")
print(f"List after removal: {my_list}\n")

# --- Tuples ---
# Tuples are ordered, unchangeable (immutable), and allow duplicate values.
print("--- TUPLES ---")
my_tuple = ("apple", "banana", "cherry")
print(f"Original tuple: {my_tuple}")

# You cannot modify a tuple directly (e.g., my_tuple[1] = "blueberry" would cause an error)
# But you can workaround this by converting it to a list and back to a tuple
temp_list = list(my_tuple)
temp_list[1] = "blueberry"
temp_list.append("orange")
my_tuple = tuple(temp_list)
print(f"Modified tuple (via list conversion): {my_tuple}")

# Unpacking a tuple
(fruit1, fruit2, *rest) = my_tuple
print(f"Unpacked: fruit1='{fruit1}', fruit2='{fruit2}', rest={rest}\n")

# --- Lists of Tuples ---
# A common use case is storing tuples inside a list
print("--- LIST OF TUPLES ---")
coordinates = [(10, 20), (30, 40), (50, 60)]
print(f"Coordinates: {coordinates}")
print(f"First coordinate's x-value: {coordinates[0][0]}")

# Adding a new coordinate (we can add to the list, but not change the existing tuples inside)
coordinates.append((70, 80))
print(f"Updated Coordinates: {coordinates}")
