arr = list(range(13))
n = 3

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=",")
    print()