# 클래스와 객체 속성
# 클래스 속성 -> 객체가 상속 받음
# 자식의 속성 변경해도 클래스의 속성은 변하지 않음
# 나중에 클래스의 속성 변경해도 이전에 생성한 객체의 속성은 변경한 클래스의 속성을 따르지 않는다(이후에 생성한 객체만 따름)

# 메소드 타입

# 정적 메소드
# @staticmethod 데커레이터 사용
# 클래스 메소드, 인스턴스 메소드가 아니므로 인수 안붙음

# 덕 타이핑
# 다형성 구현을 위한 약한 결합(개체에 따라 다르게 동작)
# who(), says() -> 리턴 타입

# 매직 메소드
# 클래스도 + 가능하게(C++에서는 연산자 오버로딩)
# 표가 따로 있음
class FlyingBehavior :
    def fly(self):
        return f"하늘을 날아갑니다"

class JetPack(FlyingBehavior):
    def fly(self):
        return f"제트팩 장착해서 날 수 있습니다"

class NoFly(FlyingBehavior) :
    def fly(self):
        return  f"하늘을 날 수 없습니다"

class FlyWithWings(FlyingBehavior) :
    def fly(self):
        return f"하늘을 날 수 있습니다"

class SwimmingBehavior :
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다"

class Pokemon3 :
    def __init__(self, name, hp, fly):
        self.__name = name
        self.hp = hp
        self.fly_behavior = fly # aggregation(has-a)

    def set_fly_behavior(self, fly):
        self.fly_behavior = JetPack()

    def attack(self):
        print("공격")

    #@property
    def get_name(self):
        print("inside getter")
        return self.name

    #@name.setter # 쓸려면 get_name 함수와 set_name 함수 이름을 모두 name으로 바꿔야 함
    def set_name(self, new_name):
        print("inside setter")
        self.__name = new_name


    # 매직 메소드
    def __str__(self):
        return self.__name + "입니다"

    def __add__(self, target):
        #return self.__name + ' + ' + target.__name
        return  f"두 포켓몬 체력의 합은 {self.hp + target.hp}입니다"

    name2 = property(get_name, set_name) # 프로퍼티
class Charizard(Pokemon3) :
    pass

class Pikachu(Pokemon3) :
    pass

nofly = NoFly()
g1 = Pikachu("피카츄", 100, nofly)
wings = FlyWithWings()
c1 = Charizard("리자몽", 120, wings)
print(g1)
print(c1)
print(g1 + c1)

print(c1.fly_behavior.fly())
print(g1.fly_behavior.fly())
g1.set_fly_behavior(JetPack())
print(g1.fly_behavior.fly())

# name과 __name의 차이?

# association(연관관계) -> has a 관계
# 상속은 is a 관계
# 상속보다 aggregation(연관관계), composition이 좋을 때가 있음
# aggregation과 composition은 보는 사람에 따라 달라짐
# aggregation은 약한 결합 composition은 강한 결합 (차이 더 찾아보자)

# composition은 객체 안에서 생성
class FlyingBehavior2 :
    def fly(self):
        return f"하늘을 날아갑니다"

class JetPack2(FlyingBehavior2):
    def fly(self):
        return f"제트팩 장착해서 날 수 있습니다"

class NoFly2(FlyingBehavior2) :
    def fly(self):
        return  f"하늘을 날 수 없습니다"

class FlyWithWings2(FlyingBehavior2) :
    def fly(self):
        return f"하늘을 날 수 있습니다"

class SwimmingBehavior2 :
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다"

class Pikachu2 :
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = NoFly2() # composition

nofly2 = NoFly2()
g2 = Pikachu2("피카츄", 35)
print(g2.fly_behavior.fly())



# chapter11
# 모듈
#import day07_mymath
#from day07_mymath import *
#import day07_mymath as mm

# if __name__ == "__main__"
