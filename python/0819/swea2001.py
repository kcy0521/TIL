# 파리퇴치
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    cnt_max = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for k in range(M):
                for o in range(M):
                    cnt += arr[i + k][j + o]

                if cnt > cnt_max:
                    cnt_max = cnt

    print(f"#{tc} {cnt_max}")
