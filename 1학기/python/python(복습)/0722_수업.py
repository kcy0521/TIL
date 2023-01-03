# 1.간단한 n의 약수

# N = int(input())

# for i in range(1,N+1):
#     if N % i == 0:
            # print(i, end=" ")

# 2. list의 합 구하기
# 정수로만 이루어진 list를 전달 받아 해당 리스트의 모든 요소들의 합을 built-in 함수인 sum()을 사용하지않고
# list_sum이라는 이름을 가진 함수로 작성하시오. 

## list_sum([1,2,3,4,5])

def list_sum(numbers): #numbers 는 정수로만 이루어진 list 다. 
    #리스트안의 요소들의 합을 저장할 변수를 선언
    sum_value = 0
    # numbers 리스트를 순회하면서 누적 합을 저장
    for number in numbers:
        sum_value += number
    return sum_value

# print(list_sum([1,2,3,4,5,6]))

## 3. Dictionary로 이루어진 list의 합 구하기
# my_dict_list = [{"name" : "kim", "age" : 12}, {"name" : "lee", "age" : 4}]

# def dict_list_sum(infos): # infos 라는 피라미터는 dictionary로 이루어진 리스트다.
#     #"age" key 에 해당해는 value들의 총 합을 저장할 변수
#     age_sum = 0
    
#     for info in infos: # infos 리스트, info 는 dictionary
#         age_sum +=info["age"]
#     return age_sum

# print(dict_list_sum(my_dict_list))


## 4. 2차원 List의 전체 합 구하기

#정수로만 이루어진 2차원 list를 전달받아 해당 list의 모든 요소들의 합을 반환하는 
# all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오. 

# my_list = [[1],[2,3],[4,5,6],[7,8,9,10]]

# def all_list_sum(num_lists): #num_lists 는 2차원 리스트이다. 
#     lists_sum = 0
#     for num_list in num_lists: #num_lists는 2차원 리스트이고 num_list 는 그 안에있는 리스트 하나
#         #num_list의 합을 구하기
#         for num in num_list: #num_list는 1차원 리스트이고, num은 그안에 있는 숫자하나. 
#             lists_sum += num
   
#     return lists_sum

# print(all_list_sum(my_list))

######### 아스키 코드를 이용해라
## 5. 숫자의 의미

# 정수로 이루어진 list를 전달받아, 각 정수에 해당하는 아스키 문자를 이어붙인 문자열을 반환하는 
# get_sevret_word 함수를 작성하시오. 단, list는 65 이상 90 이하, 97이상 122 이하의 정수로만 구성되어있다.
# (아스키 코드의 알파벳 대문자, 소문자)

# my_number = [83, 115, 65, 102, 89] # SsAfY

# def get_sevret_word(numbers): #정수로 이루어진 리스트이다. 
#     word = "" # numbers 안에있는 숫자들을 대응하는 알파벳으로 바꾼 후 이어붙일 문자열
#     for number in numbers:
#         # number 를 알파벳으로 변환
#         word += chr(number) #""chr(number)"" ==> number에 대응하는 아스키코드를 가진 알파벳 반환
    
#     return word

# print(get_sevret_word(my_number))

## 6. 내 이름은 몇일까?
# 문자열을 전달 받아서 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는
# get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다. 


# def get_sevret_number(word): #word는 '파라미터' 문자열

#     total = 0 #word의 단어 하나하나를 숫자로 바꾼 후에 그 합을 저장할 변수 

#     for char in word: #문자열 word를 문자 하나하나로 쪼갠 char // 'happy' => 'h','a','p','p','y'
#         total += ord(char) #문자를 아스키 숫자로 바꿔주는 함수 ord

#     return total

# print(get_sevret_number('happy')) #546


## 7. 강한 이름

# def get_strong_word(word1,word2):
#     word1_total = 0 
#     word2_total = 0
    
#     for char in word1:
#         word1_total += ord(char)

#     for char in word2:
#         word2_total += ord(char)

#     # 값 비교해서 결과 반환(아스키 숫자 합이 더 큰 문자열을 반환)
#     if word1_total > word2_total:
#         return word1
#     elif word2_total > word1_total:
#         return word2
#     else :
#         return word1,word2 

# print(get_strong_word("son", "park"))


## 실습 4-4 (과제) 문자열 애너그램

# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# anagram_dict = {}
# # key : 해당 단어를 정련한 결과
# # value : key와 같은 애너그램 그룹에 있는 단어들의 모으믈 리스트로 만든다. 

# for word in words:
#     sorted_word = "".join(sorted(word)) # 결과가 리스트로 나옴, 문자열로 변환해야한다. ==> join()
    
#     "".join(sorted(word))
    
#     # word = 'eat' 
#     # sorted(word) = ["a", "e", "t"]
#     # "".join(sorted(word)) = "aet"
#     # ".".join(sorted(word)) = "a.e.t" 
#     print(sorted_word)
#     if anagram_dict.get(sorted_word).append(word):
#         else:
#             anagram_dict[stored_word] = [word]

# print(anagram_dict)

# a~e 까지 프로젝트 작성해야함...


# exm = {'sdf' : 3 }
# print(exm['sdf'])
movie = {
    "adult": false,
    "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
    "genre_ids": [
        18,
        80
    ],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
    "release_date": "1995-01-28",
    "title": "쇼생크 탈출"
}

result = {}
print(movie.get('overview'))
