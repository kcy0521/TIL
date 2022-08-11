T = int(input())

for tc in range(1, T+1):
    A = int(input())
    arr = [[0]*10 for _ in range(10)] # 전체 좌표 생성해주기
    count = 0
    for a in range(A): # 색칠할 상자를 횟수 설정하기
        x1, y1, x2, y2, c = map(int, input().split())
        # 색지정은 1,2일때 색지정 어떻게 해야될까? 이점 의문
        for i in range(x2-x1 +1):
            for j in range(y2-y1 +1):
                if arr[x1+i][y1+j] != 0:
                    arr[x1+i][y1+j] = 3
                else:
                    arr[x1 + i][y1 + j] = c
    # 3인것을 찾아 보아라.
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1

    print(f"#{tc} {count}")





