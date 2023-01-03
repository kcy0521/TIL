T = int(input())

for tc in range(1, T + 1):
    m, n, k = map(int, input().split())

    arr = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1
    # 배추위치 표기 완료
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    cnt = 0
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if arr[i][j] == 1 and visited[i][j] != 0:  # 발견지점이 1이고 방문 안했을때
                    visited[i][j] = 1
                    cnt += 1
                    while 0 <= i+di[k] < n and 0 <= j+dj[k] < m and arr[i+di[k]][j+dj[k]] == 1:
                        visited[i+di[k]][j+dj[k]] = 1



