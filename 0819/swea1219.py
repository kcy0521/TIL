T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A += [a]
        B += [b]

    P = int(input())
    count = [0] * (5000 + 1)

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            count[j] += 1

    bus_stop = [int(input()) for _ in range(P)]

    print(f'#{tc} ', end='')
    for i in bus_stop:
        print(count[i], end=' ')
    print()
