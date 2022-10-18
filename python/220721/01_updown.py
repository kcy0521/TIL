import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    # 1-1. 숫자를 입력 받기(무조건 정수만 입력한다고 가정한다.)
    while True: #컨티뉴가 이쪽부터 새로 시작하게 하기위해 지정해준것. 
        number = int(input('1이상 10000이하의 숫자를 입력하세요. :'))
    # 1-2 범우 ㅣ바깥 숫자를 입력했을때, 잘못되었다고 알려준다음, 1-1로 돌아간다. 
        if number < 1 or number > 10000:
            print("잘못된 범위의 숫자를 입력했습니다. 다시 입력해주세요.")
            continue #1-1 로 돌아가야하기 때문에 반복문의 시작을 1-1에서 다시 해준다. 

        # 2-1. 플레이어가 입력한 숫자와 정답을 비교하여 up, down을 출력한다. 
        # number : 플레이어가 입력한 숫자
        # answer : 정답
        counts += 1
        
        if number > answer:
            print("Down!!")
        elif number < answer:
            print("Up!!!")
        else:
            # 2-2. 정답이라면 시도 횟수와 함께 정답 문구를 출력한다. 
            print(f"correct!!! {counts}회 만에 정답을 맞히셨습니다.")
            print()
            break #정답을 맞힌 경우 반복문을 종료한다.

    # 3. 게임 재시작 여부 파악하기
    # 3-1. 재시작 여부를 묻는 문구를 출력한다. 
    command = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. :')    
    
    # 3-2. y를 입력받으면 게임을 재시작 한다. 
    if command == "y" :
        print()
        continue #continue로 게임을 종료하지 않고 반복하도록 한다.
    
    if command == "n" :
        print()
        print("이용해주셔서 감사합니다. ^0^ ")
    else :
        print()
        print("잘못된 값을 입력하셨습니다. 게임을 종료합니다.")
    
    is_playing = False #다음 반복문에서 조건을 검사할때 false 이면 반복문을 종료한다.
