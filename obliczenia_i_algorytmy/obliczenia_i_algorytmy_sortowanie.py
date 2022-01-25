import random

list = []
for i in range(50):
    list.append(random.randint(0,100))
print("Poczatkowa lista:")
print(list)
for i in range(50):
    for j in range(i+1, 50):
        if(list[i] > list[j]):
            list[i], list[j] = list[j], list[i]
print("Posortowana lista:")
print(list)
