import shelve

class student:
    def __init__ (self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    def display(self):
        print(self.name,self.roll_no,self.marks)
        
    
db = shelve.open("student")
    
name = input("Enter the name: ")
roll_no = input("Enter the roll no:")
marks=int(input("Enter the marks:"))


s = student(name,roll_no,marks)

db[roll_no]={
    "name":name,
    "marks":marks
    }
    
search = (input("ENter the roll number to search:"))
    
if search in db:
    print("Found")
else:
    print("Not found")
    
db.close()