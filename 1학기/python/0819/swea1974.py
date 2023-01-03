# 스도쿠 검증
T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행 검사
    for i in range(9):
        if sorted(arr[i]) == test:
            result = 1
        else:
            result = 0

    # 열 검사
    for j in range(9):
        te = []
        for i in range(9):
            te += arr[i][j]
        if sorted(te) == test:
            result = 1
        else:
            result = 0

    # 3 x 3 검사
    K = [0, 3, 6]
    for k in K:
        tes = []
        for i in range(3):
            for j in range(3):
                tes += arr[i+k][j+k]

        if sorted(tes) == test:
            result = 1
        else:
            result = 0

    print(f"#{tc} {result}")
