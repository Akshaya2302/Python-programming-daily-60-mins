while True:
    print("\n1.Add 2.View 3.Exit")
    
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        amt=input("Enter the amount: ")
        with open ("expense.txt","a") as f:
            f.write(amt+"\n")
            
    elif ch==2:
        total=0
        with open ("expense.txt","r") as f:
            text=f.read()
            print(text)
            
        lines=text.split("\n")
        words=text.split()
    
        print("Lines: ",len(lines))
        print("Words:",len(words))
        print("characters: ",len(text))


        for w in words:
            if w:
                total+=float(w)

        print("Total expenses: ",total)

    elif ch==3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")