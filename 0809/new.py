T = int(input())

for t in range(1,T+1):
    K, N, M =map(int,input().split())
    
    elc = list(map(int,input().split()))
    count = 0 #충전 횟수
    
    # 마지막에까지 도착하면 반복 종료 
    # j 가 있는데 K만큼 씩을 더해준다.
    # 조건이 뭐야?
    j = 0 #현재위치
    oil = K
    while j < N: 
        j += K
        if j>=N:
            break
        while oil > 0 :
            if j in elc:
                count +=1
                break
            
            else:
                j += -1
                oil += -1
        else : 
            count = 0
            break
        
        # elif j not in elc:
        #     for i in range(1,K+1):
        #         p = j - i
        #         if p in elc:
        #             j = p
        #             count += 1
        #             break
                
        #         elif p == j-K:
        #             count = 0
        #             break
                
                    
                    


        # if j in elc:
        #     j += K
        #     count += 1
        # elif j not in elc:
        #     j += -1
        # if j == j-K: #이게 맞는 ... 건가?
        #         count = 0
        #         break
    print(f'#{t} {count}')

    # j > N 그럼 종료 
    # j + k 
    #  K마다 있으면 카운트 더해진다
    # 충전기가 K만큼 갔는데 없으면?
    # j + K -1 해준다. => 해줬는데도 없으면?
    # j + K -2 해준다. => 해줬는데도 없으면?
    # 충전기 찾으면 충전위치 갱신
    #... 위의 식대로 하다가 j == j 까지 와버린다? 글면 0을 출력