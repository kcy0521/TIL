T = int(input())

for tc in range(1, T + 1):
    A = list(range(1, 13))
    N, K = map(int, input().split())
    result = 0

    for i in range(1 << len(A)):
        sum_N = 0
        count = 0
        for j in range(len(A)):
            if i & (1 << j):
                sum_N += A[j]
                count += 1
                # 요거는 뭐를 써야할까...

        # 집합 경우의 수 항목의 합을 구해봐라.
        if count == N and sum_N == K:
            result += 1

    print(f"#{tc} {result}")
