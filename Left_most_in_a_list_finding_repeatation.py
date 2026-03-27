num = [2,3,4,5,6,4,7]
target = 4
found = False
for i in range(len(num)):
    if num[i] == target:
        print("Found")
        found = True
        break

if not found:
    print("Not found")


'''# 1. Define the list and the number we are looking for
numbers = [5, 8, 2, 7, 8, 4]
target = 8

# 2. Set a flag to keep track if we found it
found = False

# 3. Loop through the list using the index
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Success! The leftmost {target} is at index {i}.")
        found = True
        break  # We stop here because we only want the FIRST (leftmost) one

# 4. If the loop finishes and 'found' is still False, the number wasn't there
if not found:
    print("Sorry, that number is not in the list.")'''

