T = int(input())

for tc in range(1, T + 1):
    row = input() # 검사할 문자열

    stack = []

    ans = 1
    for c in row:
        if c == "(" or c == "{":
            stack.append(c)

        if c == ")" or c == "}":
            # 닫힌 괄호가 나오면 해야할 일
            # 먼저 스택의 크기를 검사해서 안에 열린 괄호가 남아있는지 확인
            if len(stack) == 0:
                ans = 0
                break

            # 열린 괄호가 있다.
            # 열린괄호의 모양이 지금 나온 닫힌 괄호의 모양과 일치하는지
            bracket = stack.pop()
            if not ((bracket == "(" and c == ")") or (bracket == "{" and c == "}")):
                ans = 0
                break
            # 남은 열린 괄호가 있는지 검사

    if len(stack) > 0:
        ans = 0

    print(f"#{tc} {ans}")


