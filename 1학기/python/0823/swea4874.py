T = int(input())

for tc in range(1, T + 1):
    n = input().split()
    k = len(n)
    result = 0
    stack = []
    # '.'으로 끝난다는것을 표현 해줘야 하고
    # 두자리수는 어떻게 할것인지를 또 표현해줘야한다.

    # 숫자면 스택에 더해준다.
    for i in range(k):
        if "0" <= n[i] <= "9":
            stack.append(n[i])

        # 숫자가 아닐때
        else:
            if n[i] == ".":
                if len(stack) == 1:
                    pass
                else:
                    result = "error"
            elif len(stack) >= 2:
                s1 = int(stack.pop())
                s2 = int(stack.pop())

                if n[i] == "+":
                    result = s2 + s1

                elif n[i] == "-":
                    result = s2 - s1

                elif n[i] == "*":
                    result = s2 * s1

                elif n[i] == "/":
                    result = s2 // s1

            stack.append(result)

    print(f"#{tc} {result}")
