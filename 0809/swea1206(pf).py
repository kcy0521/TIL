T = 10

for t in range(1, T+1):
    N = int(input()) #건물의 갯수, 빌딩이 있는 땅의 너비

    buildings = list(map(int, input().split()))

    count = 0 #조망권이 확보된 건물의 수

    for i in range(2, n-2): #양쪽 땅 2칸씩은 건물을 짖지 않는다. 
        height = buildings[i] #i 위치에 있는 빌딩의 높이
        for floor in range(height,-1,-1) : #현재 건물의 가장 위층부터 하나씩 검사
            #현재 위치에서 왼쪽 오른쪽 두칸 검사
            if floor > buildings[i-1] and floor > buildings[i-2] and floor > buildings[i+1] and floor > buildings[i+2]:
                count += 1
            else:
                #여기 밑에서부터는 검사할 필요가 없다. 
                break


    print(f"#{t} {count}")


