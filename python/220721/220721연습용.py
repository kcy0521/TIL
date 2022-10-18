## ws1. 숫자의 입력과 출력

''' 입력 받은 데이터를 숫자로 변환하고, 덧셈해서 출력하는 프로그램을 작성하시오
출력으로 숫자를 계산하여 그 결과
'''

# a = int(input('숫자 :'))
# b = int(input('숫자 :'))

# print(a + b)

## ws2. dictionary 를 활용해서 평균 구하기

''' 
좋아하는 점심메뉴를 이용하여 key = 메뉴, value = 가격 dic 만들고 점심메뉴의 평균값 출력해라

'''

# lunch = { '김밥' : 3000 , '햄버거' : 5000, '떡볶이' : 4000 }
# avg_lunch = (lunch['김밥'] + lunch['햄버거'] + lunch['떡볶이']) / 3
# print(avg_lunch)

# print(sum(lunch.values()) / len(lunch.keys()))

## hw 1.
# string, tuple, range ==> immutable
# list, set, dictionary ==> mutable

## hw 2. dict만들기
''' 반 학생들의 정보를 이용해서 key = 이름, value = 나이
'''

# student_dit = {
#     "홍길동" :30,
#     "토르" : 1500}

## hw 3. 평균구하기
#제시된 list의 평균 값을 출력하시오.

# scores = [80, 89, 99, 83]

# print(sum(score) / len(score))

# result = 0 # 누적점수 합을 저장하는 변수
# for score in scores:
#     result += score
# print(result / len(scores)) #반복문을 이용한 거임


########  220721  #####
## ws 1. 세로로 출력하기
# n1 = 10
# for i in range(1,n1 +1):
#     print(i)

## ws 2. 가로로 출력하기
# n2 = 10
# for i in range(1,n2+1):
#     print(i , end=" ")  #파라미터 인수식

## ws 3. 거꾸로 세로로 출력하기
# n3 = 5
# for i in range(n3+1)[::-1] : ##for i in range(n3,-1,-1)
#     print(i)

## ws 4. 거꾸로 가로로 출력하기
# n4 = 5
# # for i in range(n4+1)[::-1]:
# for i in range(n4,-1,-1):
#     print(i,end=' ') #end = 출력하고 끝에 붙여주세요(기본값 : 줄바꿈)

## ws 5. N줄 덧셈 
# num5 = 10

# total = 0 #누적으로 합을 저장할 함수
# for i in range(1,num5+1):
#     total = total + i

# print(total)

## ws 6. 삼각형 출력하기
num6 = 7

#왼쪽 정렬
# for i in range(1,num6+1) :
#     for j in range(1,i+1):
#         print('*', end='')
#     print() #위에서 print()함수를 호출하면 end =''로 바꿔줫기 때문에 줄바꿈이 되지 않는다.
    
#오른쪽 정렬
# for i in range(1,num6+1):
#     for j in range(num6-i,-1,-1):
#         print(' ' , end='')
#     print('*' * i)
#     # print((' '*(num6-i)) + '*'*i)


## ws 7. 중간값 찾기
# 주어진 리스트에서 중간값을 찾아 출력하는 문제
# num7 = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
# 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
# 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]
# center = len(num7) // 2
# a = sorted(num7)
# print(a[center])


### 실습 3-1  #교수님이 푼 문제로 한번 더 풀어보기
# fruit = 'apple,rottenBanana,apple,RoTTenorange,Orange'
# # good_fruit = fruit.lower().replace('rotten', '')

# fruit_list = fruit.split(',')
# fresh_list = []

# for fresh_list in fruit_list:
#     if "rotten" in fruit.lower():
#         fresh_list.append(fruit.lower().replace('rotten', ''))
#     else:
#         fresh_list.append(fruit.lower())

# print(fresh_list) # 교수님꺼로 풀어보기

### 실습 3-2 #가운데 문제를 알고싶은 문자열 입력
str1 = 'ssafy'
# if len(word) % 2 == 0 : #짝수라면 
#     print(word[len(word)//2 -1 : len(word)//2 + 1])
# else: #홀수라면
#     print(word[len(word)//2])

# result = ''
# length = len(str1)
# if length % 2 == 0 :
#     result = str1[(length //2 -1)] + str1[length //2]

# else:
#     result = str1[length //2]

# print(result)


### 3-5 . 문자열 메서드와 슬라이싱 활용

# salt = 0
# water = 0

# count = 0
# while count < 5:
#     command = input("농도 입력(Done 입력시 종료) : ")
#     if command == "Done":
#         break
    
#     density = int(command) #농도
#     brine = int(input("소금물 입력 : ")) #소금물

#     salt += density * brine #지금까지 입력받은 소금물의 총합
#     water += brine

#     count += 1

# print(f"혼합물의 농도는{salt/water :.2f} , 양은{water :.2f} 입니다".)
#.2f ==> 소수점 2번째 자리까지 출력해 주세요. / 반올림도 됨. 

## hw - 3-4
# s_string = input()
#spilt 쪼개고 그뒤에 
# map(적용할 함수 사용, 함수를 작용하고 싶은 리스트,)
# s_string.split(",")
# a,b , c map(int, t_list)
# f a ==b ==c :
# print("정삼각형)
# a =  ㅊ = a m")
# map / sprde

## 과제 2-4
'''
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders_list = orders.split(',')

#1) 아이스 음료 얼마나 들어왓는지
ice_count = 0

for drink in orders_list: #order_list를 순회하면서 drink는 계속 바뀐다. 
    #in 연산자를 통해 '아이스' 라는 문자열이 drink에 포함되어 있는지를 확인해서 포함되어있다면 ice_count를 1씩 증가
    if '아이스' in drink:
        ice_count += 1

print(ice_count)

#2) 항목별 딕셔너리 생성
orders_dict = {}
#반복문을 통해 음료의 주문횟수를 딕셔너리의 값으로, 음료의 이름을 key로 지정해서 딕셔너리를 수정해나가기
for drink in orders_list:
    if orders_dict.get(drink):
        # 값을 가져올수 있다면 조건문이 true
        orders_dict[drink] += 1
    else:
        # 제공한 키에 대한 값을 가져올수 없다면 (해당 딕셔너리에 키가 없다면) false
        orders_dict.update({drink : 1})

print(orders_dict)
for key,value in  orders_dict.items():
    print((f"{key}는 {value}잔 대기중입니다."))
'''

### 비밀번호 맞추기
"""is_pass = True
while is_pass:
    
    passowrd = 7777
    count = 0
    
    while True :
        command = int(input('비밀번호를 입력하세요 : '))
        count += 1
        
        if command != passowrd:
            print('비밀번호를 잘못 입력하셨습니다.')
            print()
            if count == 3 :
                print('비밀번호를 3회 잘못 입력 하셨습니다.')
                break
            else:
                continue       
        else :
            print('확인되었습니다.')
            break
    is_pass = False"""


matrix = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

now = [2,2]

#현재 위치가 1이라 하면
#좌표를 구해봐라
for x in range(3): # x 가 행
    print(matrix[x])
    for y in range(3):
        #행과 열을 x와 y를 통해 알수있다. 
        #현재 위치에 있는 리스트의 값이 1이다. ==> 내위치 찾기 가능
        if matrix[x][y] == 1:
            
            now[0] = x
            now[1] = y
print(f'현재 위치 : {x}행, {y}열')

