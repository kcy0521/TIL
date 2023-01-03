T = int(input())

for tc in range(1, T+1):
    n = int(input())

    paper = [[0]*10 for _ in range(10)]

    purple_count = 0

    for i in range(n):
        command = list(map(int, input().split()))
        from_i , from_j = command[0],command[1]
        to_i, to_j = command[2], command[3]
        color = command[4]

        for r in range(from_i, to_i +1):
            for c in range(from_j, to_j+1):
                if paper[r][c] == 0:
                    paper[r][c] = color

                else:
                    purple_count += 1

