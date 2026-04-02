my_list = [4,9,3,2,7,6,1]
n = len(my_list)
for i in range(n):
    for j in range(0,n-i-1):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print(f"Sorted list:{my_list}")