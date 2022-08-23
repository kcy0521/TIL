# def search(a, N, key):
#     start = 0
#     end = N - 1
#     cnt = 0
#     while start <= end:
#         middle = (start + end) //2
#         if a[middle] == key:
#             return cnt
#         elif middle > key:
#             end = middle - 1
#             cnt += 1
#         else:
#             start = middle + 1
#             cnt += 1
#     return False
#
# K = list(range(400))
#
# print(search(K,400,350))
# def f(x):
#     arr2 = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#           arr2[i][j] = x[N-1-j][i]
#     return arr2
#
#
# N = int(input())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# print(f(f(f(arr))))
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
        if len(stack) > 2:
            s1 = int(stack.pop())
            s2 = int(stack.pop())

            if n[i] == "+":
                result = s2 + s1
        #
        #     elif n[i] == "-":
        #         result = s2 - s1
        #
            elif n[i] == "*":
                result = s2 * s1
            print(result)

        #     elif n[i] == "/":
        #         result = s2 // s1
        #
        #     elif n[i] == ".":
        #         if len(stack) > 1:
        #             result = "error"
        #         if len(stack) == 1:
        #             if result == "+" or result == "-" or result == "*" or result == "/":
        #                 result = "error"
        #
        stack.append(result)
print(result)
