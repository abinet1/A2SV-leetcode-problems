import math
a = input()
a = a.split()
a=[int(i) for i in a]
w = math.ceil(a[0]/a[2])
h = math.ceil(a[1]/a[2])

print(w*h)