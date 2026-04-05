# Generating a 3x3 Identity Matrix
size = 3
matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

for row in matrix:
    print(row)
