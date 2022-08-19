def get_way_idx():
    pass

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    students = [0] * n

    for i in range(n):
        v1, v2 = list(map(int, input().split()))
        # 시작 위치는 무조건 도착 위치보다 작게
        if v1 > v2:
            v1, v2 = v2, v1
        students[i] = [v1, v2]
        # students[i][0] : 학생이 지금 잇는 방의 번호
        # students[i][1] : 학생이 가야 하는 방의 번호

        remain = n  # 자기 방으로 되돌려 보내야 하는 남은 학생수
        time = 0  # 다 보내는데 걸리는 시간
        while remain > 0:  # 학생을 다 보낼때까지 반복
            way = []
            for i in range(n):
                if students[i] != -1:
                    v1 = get_way_idx(students[i][0])  # 시작위치
                    v2 = get_way_idx(students[i][1])  # 도착위치

                move = True
                for u in way:
                    if u[0] <= v1 <= u[1] or u[0] <= v2 <= u[1]:
                        move = False
                if move:
                    way.append([v1, v2])
                    students[i] = -1
                    remain -= 1
        time += 1
    print(f"#{tc} {time}")