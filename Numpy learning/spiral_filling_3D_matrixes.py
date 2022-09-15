import numpy as np


n = 3
arr = np.full((n,n,n), -1, dtype=np.int8)
cycle = 0
directions = np.array([[0,1],[1,0],[0,-1],[-1,0]])
index = np.array([0,-1])


for i in range(1, n * n + 1):
    index = index + directions[cycle]
    if not(0 <= index[0] < n) or not(0 <= index[1] < n) or arr[0][index[0]][index[1]] > 0:
        index -= directions[cycle]
        cycle = (cycle+1)%4
        index += directions[cycle]
    arr[0][index[0]][index[1]] = i
for i in range(1,n):
    for j in range(n*n):
        arr[i][j%n][j//n] = 2*i*n*n+1 - arr[i-1][j%n][j//n]


print(arr)
