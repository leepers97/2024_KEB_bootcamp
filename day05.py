# set

# 딕셔너리처럼 키는 중복 X
# value를 가질 수 X
# 순서의 개념 X -> 순서가 중요하지 않을 때 사용

# & -> 교집합 구할 때 사용(intersection)
# | -> 합집합 구할 때 사용(union)
# - -> 차집합 구할 때 사용(difference)
# ^ -> 겹치는 것 빼고 나머지를 구할 때 사용(symmetric_difference)
# >, =, < -> 비교 연산 가능
drinks = {
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream', 'kahlua', 'vodka'},
    'manhattan' : {'rye', 'vermouth', 'bitters'},
    'screwdriver' : {'orange juice', 'vodka'}
}
print(not drinks['screwdriver'] & {'vermouth'})

# 셋 컴프리헨션
# 딕셔너리 컴프리헨션과 중괄호({}) 사용은 같으나 : 가 없음
# 리스트 컴프리헨션과 비슷할듯??
# 컴프리헨션은 for문, if문 많을 때는 가독성이 안좋아서 사용 안하는 것이 좋음

# frozenset
# 읽기 전용 -> immutable
# set과 달리 원소 삽입 등 불가



# 지금까지 데이터 구조
# 리스트, 튜플, 딕셔너리, 셋





# 함수

# 코드의 재사용성
# def

# 객체지향 원칙 : SOLID (약자임)
# S : 단일 책임의 원칙 -> 함수는 하나의 역할에 충실해야 함
# 내어쓰기 : shift + tab

def isPrime(n) -> bool :
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """

    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n :
            if n % i == 0 :
                return False
            i += 1
        return True
#help(isPrime)
#print(isPrime.__doc__)

# number_temp = input("Input first second number : ").split()
# n1 = int(number_temp[0])
# n2 = int(number_temp[1])
# if n1 > n2 :
#     n1, n2 = n2, n1
#
# for number in range(n1, n2 + 1) :
#     if isPrime(number) :
#         print(number, end = ' ')



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
#         if isPrime(number) :
#             print(f'{number} is prime number')
#         else:
#             print(f'{number} is not prime number')
#     elif menu == '4' :
#         number_temp = input("Input first second number : ").split()
#         n1 = int(number_temp[0])
#         n2 = int(number_temp[1])
#         if n1 > n2:
#             n1, n2 = n2, n1
#
#         for number in range(n1, n2 + 1) :
#             if isPrime(number) :
#                 print(number, end=' ')
#                 print()
#     elif menu == '5' :
#         print("Terminate Program")
#         break
#     else :
#         print("Wrong Input")



# 주는 쪽은 인수 받는 쪽은 매개변수

# 일반적으로는 매개변수 순서 지켜야 함
# keyword argument 사용 시 순서 안지켜도 됨
# 다만 우선 순위는 일반적인 argument 우선
# default parameter 사용 시 특정 매개변수만 지정 가능 (리스트 사용 시 호출할 때마다 초기화 X, 기존의 값 유지, 원치 않으면 리스트를 디폴트 설정 X)
# 매개변수로 *... -> 가변 매개변수 : 몇 개의 매개변수를 받을 지 모를 때 사용, 튜플로 받게 됨(파이썬은 포인터 개념 없음)
# 매개변수로 **... -> 가변 매개변수 : 몇 개의 매개변수를 받을 지 모를 때 사용, 딕셔너리로 받게 됨
# 우선순위 : 일반 -> *... -> **...
# 파이썬은 오버로딩 개념 없음
def a(n1, n2) :
    print(n1, n2)
def a(n) :
    print(n)
a(7)
#a(1, 2) -> 오류남



def aa(n) :
    if n is None :
        print(f'{n} is None')
    elif n :
        print(f'{n} is True')
    else :
        print(f'{n} is False')
aa([])
aa([0])
aa(0)
aa(None)
aa('')



# 매개변수로 **... -> 가변 매개변수 : 몇 개의 매개변수를 받을 지 모를 때 사용, 딕셔너리로 받게 됨

def squares(*n) -> list:
    """
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아 리턴
    :param n: tuple
    :return: list
    """
    return [pow(i, 2) for i in n]

def run_function(f, *number) -> list :
    return f(*number)

print(squares(7, 5, 2))
print(run_function(squares, 9, 10))



# 두 개 비교해보자
def out_func(nout) :
    def inner_func(nin) :
        return nin * nin
    return inner_func(nout)

print(out_func(5))

# closures
def out_func(nout):
    def inner_func():
        return nout * nout
    return inner_func

x = out_func(9)
print(type(x))
print(x)
print(x())



# map
# 1. 일반적인 방법
numbers = ["7", "-11", "3"]
hap = 0
for number in numbers :
    hap += int(number)
print(hap)

# 2. map 사용 방법
numbers2 = ["7", "-11", "3"]
print(sum(map(int, numbers2)))

# map 사용 - 소수 구하기(menu 4번)
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
#         if isPrime(number) :
#             print(f'{number} is prime number')
#         else:
#             print(f'{number} is not prime number')
#     elif menu == '4' :
#         n1, n2 = map(int, input("Input first second number : ").split())
#         n1, n2 = min(n1, n2), max(n1, n2)
#         # number_temp = input("Input first second number : ").split()
#         # n1 = int(number_temp[0])
#         # n2 = int(number_temp[1])
#
#         # if n1 > n2:
#         #     n1, n2 = n2, n1
#
#         for number in range(n1, n2 + 1) :
#             if isPrime(number) :
#                 print(number, end=' ')
#                 print()
#     elif menu == '5' :
#         print("Terminate Program")
#         break
#     else :
#         print("Wrong Input")



# 람다 함수
# 한 번 쓰고 버릴 때 사용
def squares2(n) :
    return n * n

even_number = [i for i in range(51) if i % 2 == 0]

# 1. 람다 미사용
print(tuple(map(squares2, even_number)))

# 2. 람다 사용
# 기본
print(tuple(map(lambda x : x**2, even_number)))
# 변수에 넣어서도 가능
z = lambda x : pow(x, 2)
print(tuple(map(z, even_number)))



# generator
# 생성 후 바로 삭제하기 때문에 메모리를 매우 적게 사용, 하지만 기억 못함
# return 대신 yield 사용 -> 값 보내고 다시 돌아옴
def my_range(first = 0, last = 10, step = 1) :
    num = first
    while num < last :
        yield num
        num += step

r = my_range()
print(r, type(r))

for x in r :
    print(x)

# 제너레이터는 기억되지 않기 때문에 두 번째부터 안찍힘
for x in r :
    print(x)

# 제너레이터 컴프리헨션



# 데코레이터
# SOLID 중 O : 개방 폐쇄 원칙 -> 확장에는 열려있고 수정에는 닫혀있어야 한다
# = 기존 코드를 수정하면 안되고 내용 추가하는데는 문제 없어야 함

# inhadeepblue

# 과제
# 242p 연습문제