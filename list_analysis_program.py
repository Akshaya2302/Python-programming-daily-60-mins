my_list = [1,2,3,4,4,5,6,7]
length = (len(my_list))
sum_of_list = sum(my_list)
maximum_in_list = max(my_list)
minimum_in_list = min(my_list)
reversed_list = list(reversed(my_list))

for i in range(my_list):
    if my_list%2==0:
        print(f"Even Integers in list:{list}")
    else:
        print(f"Odd Integers:{list}")

print(f"Length of list:{length}")
print(f"Sum of integers in a list:{sum_of_list}")
print(f"The Largest and maximun integer in a list:{maximum_in_list}")
print(f"The smallest and minimum integer in a list:{minimum_in_list}")
print(f"The Reversed list:{reversed_list}")
