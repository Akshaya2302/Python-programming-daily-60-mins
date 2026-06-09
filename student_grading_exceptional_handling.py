all_marks=[]
print("====Student Grade Analysis System====")

while True:
    try:
        user_input = float(input("Enter the marks or enter -1 to finish: "))
        
        if user_input==-1:
            break
        
        if user_input<0 or user_input>100:
            print("Marks should be between 0-100")
            
        all_marks.append(user_input)
        
    except ValueError:
        print("Invalid Marks..")
        continue
    
if len(all_marks)>0:
    for index, marks in enumerate(all_marks,start=1):
        
        if marks>=90 and marks<=100:
            print("Grade:A")
        elif marks>=80 and marks<=89:
            print("Grade:B")
        elif marks>=70 and marks<=79:
            print("Grade:C")
        elif marks>=60 and marks<=69:
            print("Grade:D")
        elif marks>=0 and marks<=59:
            print("Grade:F=fail")
   
    
    
    highest = max(all_marks)
    lowest = min(all_marks)
    average = sum(all_marks)/len(all_marks)
    
    print(f"Total Students:{len(all_marks)}")
    print(f"Highest Marks:{highest}")
    print(f"Lowest Marks:{lowest}")
    print(f"Average:{average}")
else:
    print("\n No students marks entered")
    
    