T = int(input())

for tc in range



a_start, a_end = 1,P
b_start, b_end = 1,P

while True:
    a_find = False
    b_find = False

    mid = (a_start + a_end) // 2

    if mid == a:
        a_find = True
    elif mid > a:
        a_end = mid
    else:
        a_start = mid

    # 페이지 찾기
    if mid == b:
        b_find = True
    elif mid > b:
        b_end = mid
    else:
        b_start = mid

    if a_find and b_find:
        answer = 0
        break
    if a_find:
        answer = 'A'
        break
    if b_find:
        answer = 'B'
        break