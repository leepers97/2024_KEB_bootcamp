# 과제
# 연습문제
# 1. ['Harry', ['Ron'], ['Hermione'] 리스트를 반환하는 good() 함수를 정의해보자
def good() :
    return ['Harry', 'Ron', 'Hermione']
print(good())

# 2. range(10) 의 홀수를 반환하는 get_odds 제너레이터 함수를 정의해보자. for문으로 반환된 세 번째 홀수를 찾아 출력한다
def get_odds(start = 1, end = 9, step = 2) :
    num = start
    while num <= end :
        yield num
        num += step

go = get_odds()
cnt = 0
for i in go :
    cnt += 1
    if cnt == 3 :
        print(i)
        break

# 3. 어떤 함수가 호출되면 'start를', 끝나면 'end'를 출력하는 test 데커레이터를 정의해보자
# def original() :
#     print("original")
#
# def test(func) :
#     def test_original():
#         print("start")
#         func()
#         print("end")
#     return test_original
# original = test(original)
# original()

def test(func) :
    def test_original():
        print("start")
        func()
        print("end")
    return test_original

@test
def original() :
    print("original")

original()

# 4. OopsExeption 예외를 정의해보자. 이 예외를 발생시켜보자. 그리고 이 예외를 잡아서 'Caught an oops'를 출력하는 코드를 작성해보자
class OopsException(Exception) :
    print("oops!")

try:
    raise OopsException('oops')
except OopsException:
    print('Caught an oops')


fruit1 = {'banana', 'apple'}
# fruit2 = ['banana', 'apple']
# fruit3 = ('banana', 'apple')
# fruit4 = {'banana' : 'apple'}
company = {'apple', 'microsoft'}
# print(type(fruit1))
# print(type(fruit2))
# print(type(fruit3))
# print(type(fruit4))
company.add('tesla')
print(fruit1 - company)
for i in company :
    print(i)

print(company >= fruit1)

# 셋 컴프리헨션
set_comp = {i for i in range(10) if i % 2 == 0}
print(set_comp)

# 리스트 컴프리헨션
list_comp = [i for i in range(10) if i % 2 == 0]
print(list_comp)

# 딕셔너리 컴프리헨션
dic_comp = {i : i for i in range(10) if i % 2 == 0}
print(dic_comp)


