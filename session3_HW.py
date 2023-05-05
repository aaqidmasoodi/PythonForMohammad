matrix_a = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matrix_b = [[8,2,5],
            [1,6,3],
            [11,7,0]]

result_matix = [[0,0,0],
                [0,0,0],
                [0,0,0]]

'''
set diagonal elements of both matricies to 0
'''
for i in range(3):
    matrix_a[i][i] = 0
    matrix_b[i][i] = 0


for i in range(3):
    for j in range(3):
        result_element = matrix_a[i][j] * matrix_b[i][j]
        result_matix[i][j] = result_element
        
print(result_matix)