T = int(input())

# 0~9 까지 숫자가 적힌 카드

for t in range(1,T+1):
    N = int(input()) #카드수
    nums = list(map(int,input()))

    max_card = nums[0] #카드 최대값 초기값 설정

    for x in nums:
        if x > max_card:
            max_card = x
        
    #카운팅을 넣을 빈 배열 만들기
    count_list = [0]* (max_card + 1)
    
    for i in range(N):
        count_list[nums[i]] += 1

        #출력을 위한 초기값 설정
        max_count = 0
        temp_card = 0

        for j in range(len(count_list)):
            if count_list[j] >= max_count:
                #최대값
                max_count = count_list[j]
                # 최대값의 인덱스 값이 카드 숫자를 의미
                temp_card = j

print(f'#{t} {temp_card} {max_count}')
