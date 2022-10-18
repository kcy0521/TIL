T = int(input())

for tc in range(1, T + 1):
    # N = 상자갯수 , Q = 작업수
    N, Q = map(int, input().split())
    case = [0] * (N+1)  # 작업한걸 담을 그릇
    A = [0] * Q
    B = [0] * Q

    for i in range(Q):
        l, r = map(int, input().split())
        A[i] = l
        B[i] = r

    for i in range(Q):
        for j in range(A[i], B[i]+1):
            case[j] = i+1

    print(f"#{tc}", end=' ')
    for i in range(1, N+1):
        print(case[i], end=' ')
    print()






