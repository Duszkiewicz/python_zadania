import numpy

matrix1=[]
for i in range(5):
    row=[]
    for j in range(5):
        row.append(numpy.random.randint(1, 101))
    matrix1.append(row)
print(matrix1)

print(numpy.linalg.det(matrix1))