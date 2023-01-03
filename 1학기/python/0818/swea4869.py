def f(n):
    if n == 1:
        return n
    elif n == 2:
        return n + 1
    else:
        return f(n - 1) + 2 * f(n - 2)


T = int(input())

for tc in range(1, T + 1):
    N = int(input()) // 10
    result = f(N)

    print(f'#{tc} {result}')
