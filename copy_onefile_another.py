import shelve

with open ("source.txt","r") as f:
    text=f.read()
    
with open ("target.txt","w") as f:
    f.write(text)
    
    print("File copied successfullly..")
    
lines=text.split("\n")
words=text.split()

print("Lines:",lines)
print("Words: ",words)

db = shelve.open("records")

db["23"]={
    "name": "akshu",
    "marks":95
}

roll = input("Enter the roll number: ")

if roll in db:
    print("found",db[roll])
else:
    print("Not found")    

db.close()