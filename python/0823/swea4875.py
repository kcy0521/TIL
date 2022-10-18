T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    si, sj = 0, 0
    # ni, nj = 0, 0

    # 지나온 자리 기억하기
    box = [[0] * n for _ in range(n)]

    # 시작위치 구하기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j
                # ni = i
                # nj = j
    result = 0

    while True:
        ni = si
        nj = sj
        for i in range(4):
            ni = si + di[i]
            nj = sj + dj[i]
            if box[ni][nj] != 0 and arr[ni][nj] == 0:
                box[ni][nj] += 1
            elif box[ni][nj] != 0 and arr[ni][nj] == 1:
                box[ni][nj] += 1
            elif box[ni][nj] != 0 and arr[ni][nj] == 3:
                result = 1
                break
            else:
                break

    print(f"#{tc} {result}")
