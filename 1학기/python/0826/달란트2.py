T = int(input())

for tc in range(1, T + 1):
    n, p = map(int, input().split())

    a = [n//p] * p
    b = n % p
    result = 1

    for i in range(b):
        a[i] += 1

    for i in range(len(a)):
        result *= a[i]

    print(f"#{tc} {result}")

