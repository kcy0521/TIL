# import keyword
# print(keyword.kwlist)

# num1 = 0.1 * 3
# num2 = 0.3
# import math
# print(math.isclose(num1, num2))

# \n , \t , \\  -> 이것들이 뭘 의미하는지 알기

#string Interpolation
# "안녕 철수야"
# name = "철수"
# print(f"안녕, {name}야")

# 형변환
# str(1) # (1)
# int('30')
# int(5)
# bool('50')
# int('3.5') #문자열인 것을 넣어주면 오류가 발생

# 6. 네모 출력
# n , m = 5 , 9 
# print((("*"*n) + "\n") * m)

# 7. 이스케이프 시퀀스 응용
# print()함수를 한번만 사용해서 다음 문장을 출력하시오. 
# print('"파일은 c:\\windows\\User\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')

# 8. 근의 공식
# "-b + math.sort(b*b - 4*a*c)/2*a)"
# (-b + (b*b - 4*a*c) ** (1/2)) / (2*a)

# a = set(range(2,1000,2))
# b = set(range(7,1000,7))
# # a = set(range(2,10,2))
# # b = set(range(7,10,7))
# c = (a | b)
# print(sum(c))

# 0이상 10000이하의 정수이다.
# 첫줄 테스트 케이스 개수

# # 1. 숫자의 입력과 출력
# a = int(input())
# b = int(input())

# print(a + b)

# 2. Dictionary를 활용하여 평균 구하기
menu = {'돈가스': 9000, '피자' : 27000, '햄버거' : 6000}
print(sum(int(menu)))
# print(len(menu))


