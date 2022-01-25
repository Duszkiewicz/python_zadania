import numpy
matrix1=[]
for i in range(8):
    row=[]
    for j in range(8):
        row.append(numpy.random.randint(1, 101))
    matrix1.append(row)
print(matrix1)
matrix2=[]
for i in range(8):
    row=[]
    for j in range(8):
        row.append(numpy.random.randint(1, 101))
    matrix2.append(row)
print(matrix2)
result=[]
for i in range(8):
    row=[]
    for j in range(8):
        row.append(0)
    result.append(row)

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for ele in result:
    print(ele)