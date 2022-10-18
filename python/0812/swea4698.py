def get_prime(n):
    arr = [True] * (n + 1)

    for i in range(2, n):
        if arr[i]:  # 만약 i 번째 수가 소수다
            for j in range(i + i, n + 1, i):
                arr[j] = False

    return [i for i in range(2, n + 1) if arr[i] == True]


x = get_prime(10 ** 6)

T = int(input())

for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    C = []
    count = 0
    for i in x:
        if A <= i <= B:
            C += [i]

    for j in C:
        if str(D) in str(j):
            count += 1

    print(f"#{tc} {count}")
