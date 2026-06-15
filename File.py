with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a simple file operations program in Python.\n")
    file.write("Goodbye!")

print("--- Data successfully written to example.txt ---\n")

print("--- Reading content from the file: ---")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
