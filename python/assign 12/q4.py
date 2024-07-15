def determinant(matrix):

    # using direct calculation as size of matrix is fixed ( 2 x 2 )
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return det


mat = [
    [1,2],
    [3,4]
]

print(determinant(mat))