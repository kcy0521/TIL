''' def strlen(a):
    i = 0
    while True: 
        if a[i] != '\0':
            i += 1
            

        else:
            a[0],a[i] = a[i],a[0]
            return a[1:len(a)]
            break
'''

# def strlen(a):
#     index = 0
#     while a[index] != "\0":
#         index += 1
#     return index

'''a = [ "1", "2", "3", "\0" ]

print(strlen(a))
'''

"""def my_reverse(a):
    n = len(a)
    b = []
    for i in range(n-1,-1,-1):
        b += a[i]
    return b
        
        
c ="asdsadsadavxzc"
print(my_reverse(c))"""

"""s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1 is s5) #서로 다른 메모리 할당을 받기 때문에
"""

"""def al(a, b):
    if a == b:
        return "0"
    
    i = 0
    while a[i] == b[i] :
        i += 1

        if a[i] > b[i]:
            return "-1"
            break
        else: 
            return "1"
            break"""
"""
def itoa(a):
    i = 10
    s = "" #숫자를 문자열로 바꾼 결과
    while a > 0:
        mod = a % i
        s += chr(ord('0')+mod)
        a //= 10
    return s[::-1]
a = 12345
print(itoa(a))"""
# p = "is"
# t = "This is a book~!"
# m = len(p)
# n = len(t)
#
# def BruteForce(p,t):
#     i = 0
#     j = 0
#     while j < m and i < n:
#         if t[i] != p[j]:
#             i += -j
#             j = -1
#         i += 1
#         j += 1
#     if j ==m : return i - m
#     else : return -1
#
# print(BruteForce(p, t))

"""
최소공배수, 최대공약수, 소수
최소공배수 : 두수에 서로 공통으로 존재하는 배수(공배수) 중 작은수
최대공약수 : 두수에 서로 공통으로 존재하는 약수(공약수) 중 큰수
소수 : 약수가 1 또는 자기 자신밖에 없는 숫자 (Prime number)

유클리드 호제법
2개의 자연수 a, b(a>b) 에 대해서 a를 b로 나눈 나머지가 r일때, a와 b의 최대공약수는 b와 r의 최대
공약수와 같다. 이 과정을 반복해서 나머지가 0이 되었을때, 이때 나누는 수가 a와 b의 최대공약수 이다.
"""
# 최대 공약수 구하기
# gcd : greates common divisor
def gcd(a,b):
    r = 0
    # a를 나누어 떨어질때까지 나눈다.
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

#최소 공배수
# 두 수 a와 b의 최소 공배수는 a와 b의 곱을 a와 b의 최대공약수로 나눈것과 같다.
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(6,9))
