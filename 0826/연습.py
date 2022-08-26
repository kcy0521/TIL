

arr = [[0] * 10 for _ in range(10)]
si = sj = 1
ei = ej = 4
for i in range(ei-si+1):
    for j in range(ej-sj+1):
        arr[i][j] = 1

for i in range(10):
    print(arr[i])
