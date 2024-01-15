# 주석처리 : 컨트롤 + /
# 문자열은 수정 물가능(immutable)
univ = "inha university"
subjects = ["python", "c++", "Linux", "data structure & algorithm", "database"]
print(subjects[1])

# list는 수정 가능(mutable)
subjects[1] = "C++"
print(subjects[1])



# 리터럴 : 일반적으로 오른쪽에 위치

# 변수(규칙 확인)
# 대소문자 구분, 숫자로 시작X, 예약어를 변수로 설정X
# case-sensitive
abc = 7
Abc = 8
ABC = 6
print(abc, Abc, ABC)

test9 = 77
#9test = 77
_9test9 = 77

#False = 123 # 예약어라 불가



# 할당

# type
print(type(3.14))
print(type(3.14) == float)
print(isinstance(3.14, float))
print(isinstance(55, float))

# 이거 왜 바뀌지
aa = [2, 4, 6]
bb = aa
aa[0] = 99
print(bb[0])

artists = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artists
artists[2] = '세븐틴'
print(groups)




# chapter3
# 숫자

# Bool : 0이 아닌 수는 모두 True

# 콤마 사용 X (튜플로 인식)
money = 5,000,000
print(type(money))

cash = 5_000_000 # _로 하면 가능
print(type(cash))



# 거듭제곱
base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))
# 1. f스트링
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')

# 2. format 함수
print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
print('밑은 {}, 지수는 {}, 결과 값은 {}'.format(base_number, exponent_number, pow(base_number, exponent_number)))

# 3. c like
print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_number, exponent_number, pow(base_number, exponent_number)))

