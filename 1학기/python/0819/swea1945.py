# 간단한 소인수 분해
def f(v, n):
    i = 1
    while True:
        if n % (v ** i) == 0:
            i += 1
        else:
            break
    return i - 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    a = f(2, N)
    b = f(3, N)
    c = f(5, N)
    d = f(7, N)
    e = f(11, N)

    print(f"#{tc} {a} {b} {c} {d} {e}")
