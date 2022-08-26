n = int(input())

arr = [[0] * 101 for _ in range(101)]  # 색종이가 놓일 칸
cnt = [0] * n

# 색종이 칸지정하고 확인하기
for k in range(n):
    si, sj, ei, ej = map(int, input().split())
    for i in range(ei-si+1):
        for j in range(ej-sj+1):
            arr[si+i][sj+j] = 1+k

    for n in range(101):
        for m in range(101):
            if arr[n][m] == 1+k:
                cnt[k] += 1
for i in range(101):
    print(arr[i])

for i in range(len(cnt)):
    print(cnt[i])
