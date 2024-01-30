# WAP for two matrix using list comprihension.

matrix1=[[12,34,65],[45,67,23],[67,78,23]]
matrix2=[[12,43,66],[90,78,22],[54,11,21]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix1)):
    for j in  range(len(matrix1)):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
print(result)