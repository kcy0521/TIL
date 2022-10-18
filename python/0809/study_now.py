T = int(input())

for t in range(1, T+1):

    N = int(input()) #양수의 갯수

    nums = list(map(int, input().split())) #입력받은 양수
    # 맥스와 미니멈 을 정의해라
    # result = max(num) - min(num)
    max_num = 1
    min_num = 1000000
    for num in nums:
        max_num = num if max_num < num else max_num
        min_num = num if min_num > num else min_num

    reusult = max_num - min_num

    print(f"#{t} {result}")