def tournament(i, j):
    if i == j:
        # i랑 j 가 같아지면 둘로쪼개는게 불가능 하다.
        return i
    else:
        left = tournament(i, (i + j) // 2)
        right = tournament((i + j) // 2 + 1, j)
        return winner(left, right)


def winner(l, r):
    left = num[l-1]
    right = num[r-1]

    if left == 1:
        if right == 3:
            return l
        elif right == 2:
            return r
        elif right == 1:
            return l

    elif left == 2:
        if right == 3:
            return r
        elif right == 1:
            return l
        elif right == 2:
            return l

    elif left == 3:
        if right == 2:
            return l
        elif right == 1:
            return r
        elif right == 3:
            return l


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    num = list(map(int, input().split()))

    print(f'#{tc} {tournament(1, n)}')


