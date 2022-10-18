def dfs(v, G):
    # v는 시작점, G목표지점
    visited[v] = 1  # 시작지점도 들렀다생각하고 1로 설정
    while True:
        for i in range(V+1):
            # 다음 방문 위치가 있고(1), 해당 방문위치를 방문한 적이 없으면
            if graph[v][i] == 1 and visited[i] == 0:
                stack.append(v)
                v = i
                visited[v] = 1  # 도착한 지점을 시작지점이라 생각한다
                break

        else:
            if len(stack) == 0:
                break
            else:
                v = stack.pop(-1) # 스택을 이전단계로 돌아간다.
    return visited[G]

T = int(input())

for tc in range(1, T + 1):
    # v는 꼭지점 갯수, e는 간선 정보의 수
    V, e = map(int, input().split())

    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    stack = []

    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1

    s, g = map(int, input().split())

    print(f"#{tc} {dfs(s,g)}")


