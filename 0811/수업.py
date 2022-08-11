arr = [list(map(int,input().split())) for _ in range(100)]


maxV = 0 # 맥스값 담아줄 공간
for i in range(100):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for j in range(100):
        s1 += arr[i][j]
        if maxV < s1:
            maxV = s1

    for j in range(100):
        s2 += arr[j][i]
        if maxV < s2:
            maxV = s2

    # 좌표값의 합이 99 이다.
    #  m - 1이 나오는 이유



