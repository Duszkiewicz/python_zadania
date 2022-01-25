import math

a, b, c = input("Put a, b, c:").split()
delta = int(b) * int(b) - (4 * int(a) * int(c))
if delta > 0:
     x1 = (-int(b) - math.sqrt(delta))/ (2 * int(a))
     x2 = (-int(b) + math.sqrt(delta))/ (2 * int(a))
     print("x1 =", x1)
     print("x2 =", x2)
elif delta == 0:
     x0 = (-int(b)) / (2 * int(a))
     print(x0)
else:
     print("Delta is less than zero")


