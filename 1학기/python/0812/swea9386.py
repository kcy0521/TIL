def search(p,t):
    i = 0
    j = 0
    count = 0
    max_cnt = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

        if j == M :
            count += 1
            j = 0
                if max_cnt < count:
                    max_cnt = count

    return count



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = 1
    nums = int(input())

