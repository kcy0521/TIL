def backtracking(r, sum):
    # 함수안에서 전역변수를 사용하고 싶은경우
    # 1. 수정하지않고 읽기만 한다. ==> 그냥 쓰던대로 쓰면된다.
    # 2. 수정해야한다. ==> 우리가 쓰던대로 쓰면 전역변수가 아니라 지역변수가 되어버린다.
    #   global 키워드로 전역변수를 사용한다고 꼭 선언
    # 전역변수로 쓰지 말고 함수의 파라미터로 다 가지고 다니는 방법
    global answer
    global visited

    if r == n:
        if answer > sum:
            answer = sum
        return

    # 가지치기
    if sum > answer:
        return

    for c in range(n):
        if visited[c] == 0:
            visited[c] = 1
            sum += arr[r][c]
            backtracking(r+1, sum)
            visited[c] = 0

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    answer = 100 # 값 초기화
    backtracking(0,0)

    print(f"#{tc} {answer}")
