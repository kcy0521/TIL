def drive(K,N): #버스를 운행하는 함수
    # return = 0 : 충전소가 제대로 배치되어있지 않아서 완주 불가능
    # return > 0 : 충전소가 제대로 배치되어있다. 
    last = 0 #마지막으로 충전했던 위치
    next = K #버스가 최대로 이동하는 위치(초기값은 한번 이동한 상태로)
    count = 0 # 충전한 횟수

    #종점에 도착할때까지 계속 반복
    while next < N:
        #버스가 이동한 위치에 충전기가 있나 없나 검사
        # 충전기가 없다면 뒤로 한칸씩 돌아가면서 찾을때가지 뒤로간다.
        while stop[next] == 0:
            next -= 1
            if next == last:
                return 0 #운해불가
        # 만약 뒤로 갔는데 내가 마지막으로 충전한 위치까지 와버렸다면
        # 다시 앞으로 가봤자 다시 돌아올테니까 충전소가 제대로 설치되어있지 않다.
        last = next

        next += K
        count += 1

        





T = int(input())

for t in range(1,T+1):
    k, N, M =map(int,input().split())
    
    elc = list(map(int,input().split()))
    count = 0 #충전 횟수
    
    stop = [0]*N

    for x in elc:
        stop[x] = 1