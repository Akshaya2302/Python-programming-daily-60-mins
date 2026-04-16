nums = list(map(int, input("Enter integers separated by spaces: ").split()))

print(f"\nLength  : {len(nums)}")
print(f"Sum     : {sum(nums)}")
print(f"Maximum : {max(nums)}")
print(f"Minimum : {min(nums)}")

evens = [x for x in nums if x % 2 == 0]
odds  = [x for x in nums if x % 2 != 0]
print(f"\nEven numbers : {evens}")
print(f"Odd numbers  : {odds}")

unique_sorted = sorted(set(nums))
print(f"\nUnique sorted list : {unique_sorted}")

unique = sorted(set(nums))
print(f"\nSecond smallest : {unique[1]}")
print(f"Second largest  : {unique[-2]}")

elem = int(input("\nEnter element to count: "))
print(f"{elem} appears {nums.count(elem)} time(s)")

search = int(input("Enter element to find index: "))
if search in nums:
    print(f"Index of {search} : {nums.index(search)}")
else:
    print(f"{search} not found in list")

print(f"\nReversed list : {nums[::-1]}")

positives = [x for x in nums if x >= 0]
print(f"\nList without negatives : {positives}")

average = sum(nums) / len(nums)
print(f"\nAverage : {average:.2f}")

above_avg = [x for x in nums if x > average]
print(f"Elements greater than average : {above_avg}")

print(f"\nDescending order : {sorted(nums, reverse=True)}")

print(f"\nAs a tuple : {tuple(nums)}")