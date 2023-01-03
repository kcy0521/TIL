T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())  # n은 화덕의 크기 => 한번에 넣을수 있는 피자의 양, m은 피자 개수
    ci = list(map(int, input().split()))  # 처음 뿌려진 치즈의 양
    oven = []

    # 초기 오븐 피자 설정
    for i in range(n):
        oven.append([i, ci.pop(0)])

    while True:
        for i in range(len(oven)):
            oven[i][1] = oven[i][1] // 2
            if oven[0][1] != 0:
                oven.append(oven.pop(0))

            if oven[0][1] == 0:
                for j in range(n+1, m):
                    oven.append([j, ci.pop(0)])

        if oven[0][1] == 0:

            break















