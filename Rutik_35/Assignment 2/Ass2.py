# WAP to transpose the matrix using list.

matrix =[[12,23,34],[15,65,43],[89,61,10]]

transposeM=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transposeM[i][j]=matrix[j][i]   

print("Transpose matrix : ",transposeM)


