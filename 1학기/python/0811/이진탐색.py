T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    result = ''
    s = 1
    e = P
    cnt_B = 0
    cnt_A = 0

    while s <= e:
        c = (e + s) // 2
        if A > c:
            s = c
            cnt_A += 1
        elif A < c:
            e = c
            cnt_A += 1
        else:
            break
    s = 1
    e = P
    while s <= e:
        c = (e + s) // 2
        if B > c:
            s = c
            cnt_B += 1
        elif B < c:
            e = c
            cnt_B += 1
        else:
            break

    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    else:
        result = '0'

    print(f"#{tc} {result}")
