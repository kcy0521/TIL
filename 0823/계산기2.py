T = 10

icp = {"+": 1, "*": 2}

for tc in range(1, T + 1):
    n = int(input())

    exp = input()
    postfix = ""

    stack = []
    for i in range(n):
        # 글자를 하나씩 떼서 보는데
        # 연산자 or 피연산자
        if "0" <= exp[i] <= "9":  # 문자열을 알아서 숫자열로 바꿔준다.
            postfix += exp[i]
        else:
            if stack and icp[stack[-1]] >= icp[exp[i]]:
                postfix += stack.pop()

            stack.append(exp[i])

    while stack:
        postfix += stack.pop()

    # 후위표기식 계산
    result = 0
    stack = []
    k = len(postfix)
    for i in range(k):
        # 피연산자가 나오면 그냥넘어가고
        # 스택에다가 담는다.
        if "0" <= postfix[i] <= "9":
            stack.append(postfix[i])
        else:
            right = int(stack.pop())
            left = int(stack.pop())

            if postfix[i] == "+":
                result = right + left

            else:
                result = right * left

            stack.append(result)

    print(f"#{tc} {result}")
