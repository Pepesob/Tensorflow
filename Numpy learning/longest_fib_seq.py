import numpy as np

arr1 = np.array([0,1,1,6,3,5,8,13])

count = 0
max_count = 0
a = 0
b = 1
flag = True

for n in arr1:
    while a < n and flag:
        a, b = b, a+b
    if n == a:
        count += 1
        max_count = max(max_count, count)
        flag = False
        a, b = b, a+b
    else:
        a = 0
        b = 1
        count = 0
        flag = True

print(max_count)
