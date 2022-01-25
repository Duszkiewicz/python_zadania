a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
result = 0
scalar_product = []
for i in range(len(a)):
    scalar_product.append(a[i] * b[i])
for i in range(len(scalar_product)):
    result += scalar_product[i]
print(result)