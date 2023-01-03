def BruteForce(p,t):
    i = 0
    j = 0
    count = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

        if j == M :
            count += 1
            j = 0
    return count

for tc in range(1, 11):
    T = int(input())
    word = input()
    M = len(word)
    words = input()
    N = len(words)

    print(f"#{tc} {BruteForce(word,words)}")


