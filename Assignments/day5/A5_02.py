# A5_02. Write a program to multiply two matrices as nested lists.
# Define the matrices
# A5_02. Write a program to multiply two matrices as nested lists.


matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_B = [
    [7, 8],
    [9, 10],
    [11, 12]
]


rows_A = len(matrix_A)
cols_A = len(matrix_A[0])
rows_B = len(matrix_B)
cols_B = len(matrix_B[0])

if cols_A != rows_B:
    print("Matrix multiplication is not possible.")
else:
    
    result = [[0] * cols_B for _ in range(rows_A)]

    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    
    print("The resulting matrix is:")
    for row in result:
        print(row)
