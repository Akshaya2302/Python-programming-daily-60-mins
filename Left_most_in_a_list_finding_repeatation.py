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


