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
    print("oops")

# import random
# num_list = [random.randint(1, 100) for i in range(9)]
# print(num_list)
# try:
#     pick = int(input(f'Input index (0 ~ {len(num_list) - 1})'))
#     print(num_list[pick])
#     print(5 / 0)
#     raise OopsExecption("oops") # 예외 강제로 발생시키기
# except IndexError as err: # 인덱스 범위 벗어날 때, as ...은 시스템이 던져주는 에러 메시지
#     print(f"Wrong index number\n{err}")
# except ValueError: # 문자 등 숫자 외외의 것이 왔을 때
#     print(f"Input Only Number")
# except ZeroDivisionError as err :
#     print(f"Denominator cannot be 0\n{err}")
# except OopsExecption as err :
#     print(f"Oops Oops\n{err}")
# except Exception : # 나머지 에러 (맨 아래에 있어야 함)
#     print("Error occurs")
# else :
#     print(f"Program terminated")





# chapter10
# 객체와 클래스
# 클래스 선언 후 ()는 생략 가능, ()는 상속 받을 때 필요

#class Pokemon() :
class Pokemon :
    # init은 객체마다 딱 한 번씩만 돌게 됨(생성자 느낌, 완전 같지는 않은듯, 초기화해주는 것)
    def __init__(self, name): # self는 c++로 치면 this
        self.name = name # 이 줄 덕분에 print(pikachu.name), print(squirtle.name) 가능
        print(f"{name} 포켓몬스터 생성")

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

# pikachu = Pokemon("피카츄")
# squirtle = Pokemon("꼬부기")
charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
print(pikachu.name)
print(squirtle.name)
charizard.attack(squirtle)

# 메소드 : 클래스 안에 선언된 함수

# self : c++로 치면 this, 메모리 위치 주소를 저장

# init vs new (검색해보기)
# init은 메모리를 할당하지 않음

# 상속, has a 관계, is a 관계, 의존 (검색해보기 정확 X)
# 치환 원칙 : 부모 클래스 객체가 들어갈 수 있는 곳에는 자식 클래스의 객체가 들어갈 수 있어야 한다

class Pokemon2 :
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

class Pikachu2(Pokemon2) : # is-a 관계, 자식에게 name이 없으므로 부모 class를 찾아봄
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!") # 부모클래스를 오버라이드

    def electric_info(self):
        print("전기 계열의 공격")
class Squirtle2(Pokemon2) :
    pass

p1 = Pikachu2("피카츄", "전기")
p2 = Squirtle2("꼬부기")
p3 = Pokemon2("아무개")
p1.electric_info()
p1.attack(p2)
print(p1.name, p1.type)
print(issubclass(Pikachu2, Pokemon2))

# 분류나 상속의 목적으로 추상화가 필요
# ex) 코끼리는 그릴 수 있으나 포유류는 못 그림

# super() : 부모클래스를 호출 (검색해보기)

# 다중 상속
# 두 개 이상의 부모 클래스 가짐
# 죽음의 다이아몬드 문제 생길 수 있음
# 부모 ()에 나열한 순서대로 상속됨

class Animal :
    def says(self) :
        return "동물 울음소리"

class Horse(Animal) :
    def says(self) :
        return "말 울음소리"

class Donkey(Animal) :
    def says(self) :
        return "당나귀 울음소리"

class Mule(Donkey, Horse) :
    # def says(self) :
    #     return "뮬 울음소리"
    pass

class Hinny(Horse, Donkey) :
    # def says(self) :
    #     return "히니 울음소리"
    pass

m1 = Mule()
h1 = Hinny()
print(Hinny.__mro__) # mro : 누구를 따라갈지 정함
print(Hinny.mro()) # 리스트로 반환
print(h1.says())



# Mixins
class FlyingMixin :
    def fly(self):
        return f"{self.name}이(가) 하늘을 날아갑니다"

class SwimmingMixin :
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다"

class Pokemon3 :
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("공격")

    #@property
    def get_name(self):
        print("inside getter")
        return self.name

    #@name.setter # 쓸려면 get_name 함수와 set_name 함수 이름을 모두 name으로 바꿔야 함
    def set_name(self, new_name):
        print("inside setter")
        self.name = new_name

    name2 = property(get_name, set_name) # 프로퍼티
class Charizard(Pokemon3, FlyingMixin) :
    pass

class Gyarados(Pokemon3, SwimmingMixin) :
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(g1.swim())
print(c1.fly())

c1.attack()
# Charizard.attack() # 오류남
Charizard.attack(c1) # c1.attack()과 같은 효과

# 다중상속할 때는 mro 개념(상속순서)을 잘 알고 있어야 함



# getter, setter
# 1. 직접 접근 -> 안전하지 않음
# print(g1.name)
# g1.name = "잉어킹"
# print(g1.name)

# 2. getter, setter 사용
# print(g1.get_name())
# g1.set_name("잉어킹") # 이게 맞나? 교수님 깃보자
# print(g1.set_name())

# 3. 프로퍼티 사용 (좀 더 알아보기)
print(g1.name2)
g1.name2 = "잉어킹"
print(g1.name2)

# 4. 데커레이터 사용 (좀 더 알아보기)
# @property, @name.setter로 getter, setter 사용
# get_name, set_name 함수 등록 과정 생략 가능



# 변수 앞에 __ 붙이면 직접 접근 불가, 프로퍼티로만 접근(private 비슷하게, private 개념은 없음 그냥 따라한거)
# 함수랑 이름 같아야하는듯? ex) print(g1.__name)
# 근데 이건 됨 print(g1._Pokemon3__name) -> 같은 클래스에서 접근 가능


# 과제
# 포켓몬 게임 만들기
# 기획 필요
# 클래스 설계
# 어떤 기능이 있을지(ex) 진화 등)
# 텍스트 기반으로 만듬
# ex) 시작하고 포켓몬 고름 -> 고른 포켓몬 객체 생성 -> 적 만나기 -> 전투, 도망 등
# 리스트 딕셔너리 활용하여 레벨 별 스킬 등
# 도망 매뉴얼(랜덤 등 사용)
# 속성별 상성
# getter setter, 데커레이터, 함수활용 등 여러 개 사용해보자
