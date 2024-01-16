# 과제
# 1. 1번 2번 화씨 섭씨 3번 메뉴가 소수 판정 프로그램 4번 메뉴가 구간 소수 출력 5번 종료
# 2. 143p 연습문제 6.5번 - 1, 2, 3

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
#                     print()
#     elif menu == '5' :
#         print("Terminate Program")
#         break
#     else :
#         print("Wrong Input")



# 연습문제 6-5
# 1. for문으로 리스트 [3, 2, 1, 0] 출력
pracList = [3, 2, 1, 0]
for pl in pracList :
    print(pl, end = ' ')
    print()



# 2. guess_me 변수에 7을 할당하고, number 변수에 1을 할당한다. number와 guess_me를 비교하는 while문을 작성해보자. number가 guess_me보다 작으면 'too low'를 출력한다.
#    같으면 'found it!'을 출력하고 반복문을 종료한다. 크면 'oops'를 출력하고 반복문을 종료한다. 그리고 반복문의 마지막에 number를 1씩 증가시킨다.
# guess_me = 7
# number = 1
# while True :
#     if number < guess_me :
#         print('too low')
#     elif number == guess_me :
#         print('found it!')
#         break
#     else :
#         print('oops')
#         break
#     number += 1



# 3. guess_me 변수에 5를 할당하고 for문을 사용하여 range(10)에서 number변수를 사용한다. number가 guess_me보다 작으면 'too low'를 출력한다. 같으면 'found it!'을
#    출력하고 반복문을 종료한다. 크면 'oops'를 출력하고 반복문을 종료한다.
guess_me = 5
for number in range(10) :
    if number < guess_me:
        print('too low')
    elif number == guess_me :
        print('found it!')
        break
    else :
        print('oops')
        break