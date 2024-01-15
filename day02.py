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
