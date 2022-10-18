T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    N_list = list(map(int, input().split()))
    
    maxadd = 0
    minadd = 10000000000 #임의 설정
    
    for i in range(N-M+1): # 전제 범위가져오기
        result = 0
        for j in range(i,i+M): #구간범위 가져오는거
            
            result += N_list[j] 

        if maxadd <= result:
            maxadd = result
        if minadd >= result:
            minadd = result
    print(f'#{t} {maxadd-minadd}')