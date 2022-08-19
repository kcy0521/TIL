# 90도 만큼 회전시키는 함수
def f(x):

    arr2 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
          arr2[i][j] = x[N-1-j][i]


    return arr2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90 도 회전 180도 회전 270 회전한 모양을 출력하라
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f(arr)[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(f(f(arr))[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(f(f(f(arr)))[i][j], end='')
        print(end=' ')
        print()