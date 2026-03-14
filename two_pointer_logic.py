target = input("Enter the Word:")
typed = input("Enter the mistyped word:")

i = 0
j = 0 #j is P which is a string in the statement , 
       #Where it is a mistyped word
final_word=""
while i<len(target) and j<len(typed):
   if target[i]==typed[j]:
      i+=1
      final_word+=typed[j]
   j+=1

if i == len(target):
    deletions = len(typed)-len(target)
    print(f"Original Word:{target}")
    print(f"Mistyped Word:{typed}")
    print("Deleted words are:",deletions)
    print(f"After deletions in mistyped word:{final_word}")
else:
    print("IMPOSSIBLE")


