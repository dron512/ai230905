import numpy as np

a = [10,20,30,40,50]
na = np.array(a)

print(a[0])
print(na[0])

for idx, item in enumerate(a):
    a[idx] = (item+10)

print(a)
print(na + 10)
