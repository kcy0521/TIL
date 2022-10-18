T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    qq = []
    si = 0
    sj = 0
    cnt = 0

    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j

    ans = True
    visited[si][sj] = 1
    qq.append((si, sj))
    while qq and ans:  # 길을 못찾을 때까지 진행해라~
        cnt += 1
        for i in range(len(qq)):
            (a, b) = qq.pop(0)
            for j in range(4):
                ni = a + di[j]
                nj = b + dj[j]
                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                    if arr[ni][nj] == 3:
                        ans = False
                        break
                    qq.append((ni, nj))
                    visited[ni][nj] = 1
    if ans:
        print(f'#{tc} 0')
    else:
        print(f"#{tc} {cnt -1}")
