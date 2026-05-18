# String Basics in Python

# 1. Creating strings
greeting = "Hello, World!"
name = 'Python'
multiline = """This is
a multiline
string."""

print("--- Creating Strings ---")
print(greeting)
print(name)
print(multiline)

# 2. String indexing & slicing
print("\n--- Indexing & Slicing ---")
word = "Programming"
print(f"First char: {word[0]}")       # P
print(f"Last char: {word[-1]}")       # g
print(f"Slice [0:4]: {word[0:4]}")    # Prog
print(f"Reverse: {word[::-1]}")       # gnimmargorP

# 3. Common string methods
print("\n--- String Methods ---")
text = "  hello python  "
print(f"Upper: {text.upper()}")
print(f"Strip: '{text.strip()}'")
print(f"Replace: {text.replace('python', 'world')}")
print(f"Split: {'a-b-c'.split('-')}")
print(f"Join: {'-'.join(['x', 'y', 'z'])}")

# 4. String formatting
print("\n--- Formatting ---")
language = "Python"
version = 3.12
print(f"{language} version {version}")                   # f-string
print("{} version {}".format(language, version))         # .format()

# 5. Checking strings
print("\n--- Checks ---")
print(f"'hello'.isalpha(): {'hello'.isalpha()}")         # True
print(f"'123'.isdigit(): {'123'.isdigit()}")             # True
print(f"'Py' in 'Python': {'Py' in 'Python'}")          # True
print(f"'Python'.startswith('Py'): {'Python'.startswith('Py')}")  # True
