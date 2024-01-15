# 주석처리 : 컨트롤 + /
# 문자열은 수정 물가능(imutable)
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
