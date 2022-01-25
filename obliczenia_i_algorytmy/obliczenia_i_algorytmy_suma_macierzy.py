import numpy
import random

matrix1=[]
for i in range(128):
    row=[]
    for j in range(128):
        row.append(numpy.random.randint(1, 101))
    matrix1.append(row)
print(matrix1)
matrix2=[]
for i in range(128):
    row=[]
    for j in range(128):
        row.append(numpy.random.randint(1, 101))
    matrix2.append(row)
print(matrix2)
result=[]
for i in range(128):
    row=[]
    for j in range(128):
        row.append(0)
    result.append(row)
for i in range(len(matrix1)):
   for j in range(len(matrix1[0])):
       result[i][j] = matrix1[i][j] + matrix2[i][j]
for ele in result:
   print(ele)