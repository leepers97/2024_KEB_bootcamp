# 데커레이터 보충
def desc(f) :
    def wrapper() : # wrapper는 실행 X, clouser
        print("study")
        f()
    #print("a")
    return wrapper

@ desc
def something() :
    print("do something")
something()

# 네임스페이스와 스코프
# 전역변수가 있을 때 지역변수에서 그 전역변수를 바꿔도 함수 안에서만 바뀜
# 함수 내에서 global 변수이름 선언 후 변경 -> 전역변수를 함수에서 바꿔도 전역변수가 변경됨
# 전역변수는 메모리를 계속 소모함 -> 남발하지 않는 것이 좋음

# 변수에 _ 두 개 같이 붙이지 않기



# 재귀
# 팩토리얼 예제
# 1. 반복문 사용
def factorial_1(n) -> int:
    result = 1
    for i in range(2, n+1) :
        result *= i
    return  result
# print(factorial_1(int(input("number : "))))

#2. 재귀 사용
def factorial_2(n) -> int :
    if n == 1 :
        return n
    else :
        return n * factorial_2(n - 1)
# number = int(input("number : "))
# print(factorial_2(number))

# 재귀는 실수가 나오기 적으나 반복문보다 느림



# 비동기 함수
# 속도가 빠름
# 딱히 중요하지는 않은듯



# 예외 처리

# 직접 예외 만들기
# 왜 oops 발동 안하지
class OopsExecption(Exception) :
    pass

import random
num_list = [random.randint(1, 100) for i in range(9)]
print(num_list)
try:
    #pick = int(input(f'Input index (0 ~ {len(num_list) - 1})'))
    #print(num_list[pick])
    print(5 / 0)
    raise OopsExecption("oops") # 예외 강제로 발생시키기
except IndexError as err: # 인덱스 범위 벗어날 때, as ...은 시스템이 던져주는 에러 메시지
    print(f"Wrong index number\n{err}")
except ValueError: # 문자 등 숫자 외외의 것이 왔을 때
    print(f"Input Only Number")
except ZeroDivisionError as err :
    print(f"Denominator cannot be 0\n{err}")
except OopsExecption as err :
    print(f"Oops Oops\n{err}")
except Exception : # 나머지 에러 (맨 아래에 있어야 함)
    print("Error occurs")
else :
    print(f"Program terminated")





# chapter10
# 객체와 클래스
# 클래스 선언 후 ()는 생략 가능, ()는 상속 받을 때 필요

#class Pokemon() :
class Pokemon :
    # init은 객체마다 딱 한 번씩만 돌게 됨(생성자 느낌)
    def __init__(self, name): # self는 c++로 치면 this
        print(f"{name} 포켓몬스터 생성")

pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
