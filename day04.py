# 과제
# 1. 1번 2번 화씨 섭씨 3번 메뉴가 소수 판정 프로그램 4번 메뉴가 구간 소수 출력 5번 종료
# 2. 143p 연습문제 6.5번 - 1, 2, 3
#
# 1.
# while True :
#     menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3. Judge Prime number   4. Range based prime number   5) Quit program : ")
#     if menu == '1' :
#         fahrenheit = float(input("Input Fahrenheit : "))
#         print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5 / 9) : .4f}C')
#     elif menu == '2' :
#         celsius = float(input("Input Celsius : "))
#         print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9 / 5) + 32) : .4f}C')
#     elif menu == '3' :
#         number = int(input("Input number : "))
#         isPrime = True
#         if number < 2 :
#             print(f'{number} is not prime number')
#         else :
#             for i in range(2, number) :
#                 if number % i == 0 :
#                     isPrime = False
#                     break
#             if isPrime :
#                 print(f'{number} is prime number')
#             else :
#                 print(f'{number} is not prime number')
#     elif menu == '4' :
#         number_temp = input("Input first second number : ").split()
#         n1 = int(number_temp[0])
#         n2 = int(number_temp[1])
#         if n1 > n2:
#             n1, n2 = n2, n1
#
#         for number in range(n1, n2 + 1):
#             isPrime = True
#             if number < 2:
#                 pass
#             else:
#                 for i in range(2, number):
#                     if number % i == 0:
#                         isPrime = False
#                         break
#                 if isPrime:
#                     print(number, end=' ')
#         print()
#     elif menu == '5' :
#         print("Terminate Program")
#         break
#     else :
#         print("Wrong Input")

# 개선사항
# 1. 4번 : 소수일 경우 for문 과하게 돌아감
# 2. 4번 : 입력 받는 부분 불친절
# 3. 중복 코드 제거
# 4. 라이브러리 가져오는 것 고려

# while True :
#     menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3. Judge Prime number   4. Range based prime number   5) Quit program : ")
#     if menu == '1' :
#         fahrenheit = float(input("Input Fahrenheit : "))
#         print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5 / 9) : .4f}C')
#     elif menu == '2' :
#         celsius = float(input("Input Celsius : "))
#         print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9 / 5) + 32) : .4f}C')
#     elif menu == '3' :
#         number = int(input("Input number : "))
#         isPrime = True
#         if number < 2 :
#             print(f'{number} is not prime number')
#         else :
#             for i in range(2, number) :
#                 if number % i == 0 :
#                     isPrime = False
#                     break
#             if isPrime :
#                 print(f'{number} is prime number')
#             else :
#                 print(f'{number} is not prime number')
#     elif menu == '4' :
#         number_temp = input("Input first second number : ").split()
#         n1 = int(number_temp[0])
#         n2 = int(number_temp[1])
#         if n1 > n2:
#             n1, n2 = n2, n1
#
#         for number in range(n1, n2 + 1):
#             isPrime = True
#             if number < 2:
#                 pass
#             else:
#                 i = 2
#                 while i * i <= number :
#                     if number % i == 0:
#                         isPrime = False
#                         break
#                     i += 1
#                 if isPrime:
#                     print(number, end=' ')
#         print()
#     elif menu == '5' :
#         print("Terminate Program")
#         break
#     else :
#         print("Wrong Input")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter 7
# 튜플과 리스트

# tuples
# 괄호 없이도 사용 가능
# 최소 한 개 이상의 콤마 필요
t1 = (5) # int
t2 = 5,
t3 = (5, )
t4 = (5, 7)
t5 = 5, 7
t6 = "python", "kim" # packing
print(type(t1), type(t2), type(t3),  type(t4),  type(t5), type(t6))
print(t6[1])

# unpacking (잘 이해 안됨 다시보기)
# 언패킹은 개수 맞아야 함
# a, b, c = t6 불가
subject, prof = t6
print(prof)
print(subject)

# 빈 튜플은 튜플로 처리(예외)
t7 = ()
t8 = tuple()
print(type(t7), type(t8))

# + 내용
aaa = 'aaa',
print(type(aaa))
print(type('aaa',)) # string
print(type(('aaa',))) # tuple

# 튜플에서의 +, * 연산 책보기

# 튜플간 비교 연산
# 원소 순서대로 계산
t9 = 1, 2, 3
t10 = 1, 2
print(t9 == t10)
print(t9 <= t10)
print(t9 > t10)

# 튜플 간 더하기 가능
t11 = 4.43,
t12 = 3.97, 4.1, 3.2
print(t11 + t12)
print(id(t11))
t11 += t12 # t11의 id가 바뀜 -> immutable하므로 바뀐 것이 아니라 새로 만든 것을 t11에 연결한 것
print(id(t11))
print(t11)

# 풀었던 문제에서 n1 n2쪽 다시 봐보기

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# list
# 아무거나 다 담을 수 있음, but 그러면 성능 이슈 발생

# 튜플 -> 리스트 형변환 (튜플은 값 수정이 안되므로 리스트로 바꿔서 수정하고 다시 바꾸기 가능, 다만 그 튜플은 이름만 같고 새로운 튜플임)
a_tuple = ('aaa', 'bbb', 'ccc')
print(type(a_tuple))
print(type(list(a_tuple)))

# split : 문자열을 list로 변환

# 역방향 인덱싱 가능

# 슬라이싱 가능

# 역방향
subjects = ["C++", "Java", "Python", "Java"]
print(subjects[::-1]) # 원본을 바꾸지 않음
print(subjects)
subjects.reverse() # 원본을 바꿈
print(subjects)



#원소 추가
# append()
# 리스트 맨 뒤에 원소 삽입

# insert()
# 원하는 곳에 원소 삽입, but 자료 많을 경우 느림 -> 교수님은 잘 안씀

# 리스트의 결합
# extend() 혹은 += 사용
# extend()는 원본 바꾸고 +=는 업데이트

# mutable하므로 값 변경 가능
# 슬라이싱으로도 값 변경 가능
subjects[:1] = ["C"]
print(subjects)



# 원소 삭제
# del, remove() 사용
# remove는 같은 값이 있으면 맨 앞의 값만 삭제
subjects.remove("Java")
# del subjects[2]
print(subjects)

# pop()
# 맨 뒤를 삭제 -> 속도가 빠름
# 삭제 후 리턴

# clear()
# 모든 원소 삭제



# in
# 해당 값이 있으면 True를 반환, 없으면 False를 반환
print("C" in subjects)

# join(), split()
# 어제 배운 것과 같음

# sort(), sorted()
# sort는 원본을 바꾸지만 sorted는 원본을 유지하고 사본을 생성
# list 안에 자료형이 다르면 오류남
subjects.sort()
# subjects.sort(reverse = True) # 역순으로
print(subjects)

copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects)



# 얕은 복사, 깊은 복사
# mutable한 값을 바꾸면 얕은 복사 한 것들은 모두 바뀜
# 바뀌는 것을 원치 않으면 깊은 복사 해야 함
import copy
#sub = ["a", "b", "c"]
sub = ["a", ["b", "c"], "d"]
a = sub
b = sub.copy()
c = list(sub)
d = sub[:]
e = copy.deepcopy(a)
print(sub, a, b, c, d, e)

#sub[1] = "x"
print(id(a), id(b), id(c))
sub[1][1] = "x"
#sub[0] = "x"
print(sub, a, b, c, d, e) # 깊은 복사한 e만 바뀌지 않음
print(id(sub), id(a), id(b), id(c))

# 리스트가 튜플보다 기능이 많지만 성능은 튜플이 좋음(메모리 적게 차지, 실수로 바뀔 일 없음, 딕셔너리의 키값으로 사용 가능(딕셔너리의 키값은 immutable 해야함))

# zip()
# 가장 적은 수의 리스트를 기준으로 여러 개의 컨테이너를 돌릴 수 있음



# 값 추가하는 짧고 간편한 방법 (list comprehension)
# 1. 무식한 방법
# squares = list()
# squares.append(1 * 1)
# squares.append(2 * 2)
# squares.append(3 * 3)
# squares.append(4 * 4)
# squares.append(5 * 5)

# 2. for문 사용
# squares = list()
# for i in range(1, 6, 1) :
#     squares.append(i * i)
# print(squares)

# 3. list comprehension(축약 표현) 사용
squares = [i * i for i in range(1, 6, 1)]
print(squares)

# list comprehension 사용 + 조건 달기
even_squared = [i * i for i in range(1, 6, 1) if i % 2 == 0]
print(even_squared)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter 8
# 딕셔너리, 셋

# 딕셔너리
# {} (중괄호) 사용
# :쓰기 귀찮으면 dict함수를 사용(다만 그러면 변수 이름에 공백이나 예약어 사용 불가능)
# 튜플이나 리스트를 딕셔너리화 가능
# mutable
sugang = dict(python = "kim", db = "kang", cpp = "sung")
sugang["data structure"] = "kim" # 추가
sugang["data structure"] = "park" # 수정
print(sugang)
print(sugang["db"])
print(sugang.get("db"))
# get() 사용 시 두 번째 인수로 찾지 못했을 경우 어떻게 출력할지 정할 수 있음
print(sugang.get("open source", "not exist"))



for subj, professor in sugang.items() : # subj는 키, professor는 값
    print(f'{subj} 과목 담당교수는 {professor}입니다')

# keys()
# 키값들만 꺼내줌
for k in sugang.keys() :
    print(k)

# values()
# 밸류값들만 꺼내줌
for v in sugang.values() :
    print(v)

# items
# 키값과 밸류값 모두 꺼내줌
# 튜플에 담겨서 나옴
for s in sugang.items() :
    print(s)



# 딕셔너리를 이용한 술안주 추천
import random
drink_foods = {"위스키" : "초콜릿", "와인" : "치즈", "소주" : "삼겹살", "고량주" : "양꼬치"}
#del drink_foods["위스키"]
#drink_foods["사케"] = "광어회"
japan_drinks_foods = {"사케" : "광어회", "위스키" : "낙곱새"} # 위스키를 덮어씀
drink_foods.update(japan_drinks_foods)

#drink = input(drink_foods.keys())
drink_foods_keys = list(drink_foods)
# drink = input(f"다음 술 중에 고르세요\n1) {drink_foods_keys[0]}  2) {drink_foods_keys[1]}  3) {drink_foods_keys[2]}  4) {drink_foods_keys[3]} : ")
# print(drink_foods[drink])
# print(random.choice(drink_foods_keys)) # 튜플, 리스트 등 가능
# while True :
#     menu = input(f"다음 술 중에 고르세요\n1) {drink_foods_keys[0]}  2) {drink_foods_keys[1]}  3) {drink_foods_keys[2]}  4) {drink_foods_keys[3]}  5) {drink_foods_keys[4]}  6) 아무거나  7) 종료: ")
#     if menu == '1' :
#         print(f'{drink_foods_keys[0]}에 어울리는 안주는 {drink_foods[drink_foods_keys[0]]} 입니다')
#     elif menu == '2' :
#         print(f'{drink_foods_keys[1]}에 어울리는 안주는 {drink_foods[drink_foods_keys[1]]} 입니다')
#     elif menu == '3' :
#         print(f'{drink_foods_keys[2]}에 어울리는 안주는 {drink_foods[drink_foods_keys[2]]} 입니다')
#     elif menu == '4' :
#         print(f'{drink_foods_keys[3]}에 어울리는 안주는 {drink_foods[drink_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'{drink_foods_keys[4]}에 어울리는 안주는 {drink_foods[drink_foods_keys[4]]} 입니다')
#     elif menu == '6':
#         random_drink = random.choice(drink_foods_keys)
#         print(f'{random_drink}에 어울리는 안주는 {drink_foods[random_drink]} 입니다')
#     elif menu == '7' :
#         print(f'다음에 또 오세요')
#         break



# 딕셔너리 합치기
# {**a, **b}
# 겹치면 나중 것이 오버라이트(덮어씀)
# 얕은 복사

# update()
# 기존 딕셔너리를 업데이트함(추가)
# 만약 두 딕셔너리의 키가 같다면 두 번째 딕셔너리가 덮어쓴다



# 딕셔너리 삭제
# 1. del

# 2. pop()
# 삭제 후 리턴
# 없애는 내용이 없을 시 두 번째 인자에 넣은 내용 출력 가능



# 튜플을 딕셔너리 키로 사용할 때
a = {(1, 2) : 3, (5, 4) : 9}
print(a)
print(a[(1, 2)])

# 딕셔너리 컴프리헨션
# 리스트도 컴프리헨션 있는데 튜플은 없음
univ = 'inha university'
counts_alphabet = {letter : univ.count(letter) for letter in univ}
print(counts_alphabet)

counts_alphabet2 = dict() # 풀어쓰면 이렇게
for letter in univ :
    counts_alphabet2[letter] = univ.count(letter)
print(counts_alphabet2)

# b = {[1, 2] : 3, [5, 4] : 9} # 리스트는 mutable하므로 키값에 쓸 수 없어 오류남
# print(b)
# 과제
# 205p 연습문제 8.10까지 (10문제)

# 10. 딕셔너리 컴프리헨션으로 squares딕셔너리를 생성한다. range(10)을 키로 하고, 각 키의 제곱을 값으로 한다
squares = {i : pow(i, 2) for i in range(10)}
print(squares)
