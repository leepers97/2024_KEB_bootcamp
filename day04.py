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



# list
# 아무거나 다 담을 수 있음, but 그러면 성능 이슈 발생

# 튜플 -> 리스트 형변환 (튜플은 값 수정이 안되므로 리스트로 바꿔서 수정하고 다시 바꾸기 가능, 다만 그 튜플은 이름만 같고 새로운 튜플임)
a_tuple = ('aaa', 'bbb', 'ccc')
print(type(a_tuple))
print(type(list(a_tuple)))
