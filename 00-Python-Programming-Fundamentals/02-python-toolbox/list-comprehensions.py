# Create list comprehension: squares
squares = [i ** 2 for i in range(10)]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5) ]

# Print the matrix
for row in matrix:
    print(row)
