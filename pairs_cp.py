
k = 1                    
arr = [1,2,3,5,4]        


num_set = set(arr)
count = 0

for x in arr:
    
    partner = x - k
    
    if partner in num_set:
        count = count + 1

print(count)