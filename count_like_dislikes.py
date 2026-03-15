def count_like_dislike(A, P):
    
    total_matches = 0
    
    for i in range(len(A)):
 
        if A[i] == P[i]:
            total_matches += 1
            
    return total_matches

# Get the inputs
A = (input("Enter the likes and dislikes of Bob:"))
P = (input("Enter the likes and dislikes of alice:"))

total_matches = count_like_dislike(A, P)
print(total_matches)