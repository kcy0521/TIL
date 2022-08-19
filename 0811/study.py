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
def f(x):
    arr2 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
          arr2[i][j] = x[N-1-j][i]
    return arr2


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

print(f(f(f(arr))))

