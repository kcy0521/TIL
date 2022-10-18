di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    q = [(si, sj)]

    maze[si][sj] = 1

    while q:
        i, j = q.pop(0)

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1:
                if maze[ni][nj] == 3:
                    return 1
            maze[ni][nj] = 1
            q.append((ni, nj))

    return 0


for T in range(10):
    tc = int(input())

    n = 16

    maze = [list(map(int, input())) for _ in range(n)]

    si = sj = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                si, sj = i, j

    print(f"{tc} {bfs(si,sj)}")