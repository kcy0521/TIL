T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())  # n은 주어진 갯수, m = 반복 횟수
    arr = list(map(int, input().split()))

    qq = []

    for i in range(m): # 회 반복해라
        arr.append(arr.pop(0))

    result = arr[0]

    print(f"#{tc} {result}")


'''
queue = arr
front = 0 

for i  in range(n):
    front = (front +1) % n 
queue
'''