# 예습 문제
# 섭씨 화씨 3번을 누르기 전에는 계속 프로그램이 돌아가게

'''while True :
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
    if menu == '1' :
        fahrenheit = float(input("Input Fahrenheit : "))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5 / 9) : .4f}C')
    elif menu == '2' :
        celsius = float(input("Input Celsius : "))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9 / 5) + 32) : .4f}C')
    elif menu == '3' :
        print("Terminate Program")
        break
    else :
        print("Wrong Input")'''


# 초대코드 : vxrbjug

# text strings
# 아스키코드 보기 ex) 65 = a
# mutable - list, set, dictionary,byte array
# 전체적인 내용 책으로 한 번 보기
# ''', """ : 사이에 다른 따옴표 마음껏 사용 가능
# \n : 줄바꿈
# \\ : \ 자체를 출력
# raw string : r'...' -> 이스케이프 문자 자체를 출력
university = r"Inha\nUniversity"
print(university)



# 문자 결합
# +를 이용하여 결합 가능
#number1 = input("First Number : ")
#number2 = input("Second Number : ")
#print(number1 + number2) # int로 형변환하지 않아 문자열 결합

# () 이용하여 결합 가능

# *를 이용하여 문자열 반복 가능
#print(number1 * 3)

# []로 역방향 인덱싱 가능
#print(number1[1])

# 문자열은 immutable이므로 number[1] = 'P' 이런거 불가능
# 하지만 replace로 교체 가능 (뭔가 틀렸는데 책보기 + 슬라이싱)
name = 'Henny'
name.replace('H', 'P')
print(name)

# slicing (자세히 알아보기)
# [:] : 처음부터 끝까지
# [start :] : start부터 끝까지
# [: end] : 처음부터 end까지
# [start : end] : start부터 end까지 -1
# [start : end : step] : step만큼 증가
univ = "InhaUniversity"
print(univ[: 4])
print(univ[:-10])
print(univ[:len(univ)])

# len : 문자열의 길이



# split (중요함)
# 문자열을 list로
course = "2024 KEB Bootcamp"
#list_course = course.split()
list_course = course.split('B') # B가 구분자
print(list_course)

# number = input("FirstNumber SecondNumber : ").split()
# print(number[0] + number[1]) # 결합
# print(int(number[0]) + int(number[1])) # 산술 연산



# join (중요함)
# list를 문자열로
subjects = ["python", "c++", "database"]
subjects_string = " / ".join(subjects)
print(subjects_string)


# replace
course2 = "KEB 2024 KEB Bootcamp"
# print(course2)
# print(course2.replace("KEB", "Inha"))
# print(course2)
# course2 = course2.replace("KEB", "Inha")
# print(course2)

print(course2)
print(course2.replace("KEB", "Inha"))
print(course2.replace("KEB", "Inha", 1))
print(course2)



# strip
# strip : 양쪽 빈공간 삭제
# lstrip : 왼쪽 빈공간 삭제
# rstrip : 오른쪽 빈공간 삭제
course3 = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course3.strip("!#.*")) # 양쪽 끝 연속적인 것만 건들임



# 부록2 참고



# 함수 몇 개
# startswith('...') : ...으로 시작하는 문자열이 있으면 true값 반환
# find('...') : ...의 index를 반환, 찾지 못하면 -1 반환
print(course3.find("KEB"))
print(course3.rfind("KEB")) # 뒤에서부터 찾기
print(course3.index("KEB"))
print(course3.find("Inha"))
#print(course3.index("Inha")) # index는 찾지 못하면 예외 던짐(오류)

subject = "python c++ database linux"
subject2 = input("수강신청과목 입력 : ")
# if subject.find(subject2) != -1:
#     print(f'해당 과목은 존재합니다. 그리고 위치는 {subject.find(subject2)}번 인덱스입니다.')
# else:
#     print('해당 과목이 존재하지 않습니다')

# index를 이용하면 존재하지 않을 때 오류남
# if subject.index(subject2) != -1:
#     print(f'해당 과목은 존재합니다. 그리고 위치는 {subject.index(subject2)}번 인덱스입니다.')
# else:
#     print('해당 과목이 존재하지 않습니다')

# -> 예외처리 해주기
try :
    print(f'해당 과목은 존재합니다. 그리고 위치는 {subject.index(subject2)}번 인덱스입니다.')
except ValueError :
    print('해당 과목이 존재하지 않습니다')

# count
# 몇 개 있는지 세는 함수

# isalnum
# 알파벳만 있는지 검사하여 true 혹은 false 반환(띄어쓰기도 안됨)
print(subject.isalnum())

# title
# 띄어쓰기마다 첫글자를 대문자로

# upper
# 전부 대문자로

# 정렬
# center : 가운데 정렬
# ljust : 왼쪽 정렬
# rjust : 오른쪽 정렬

# %표기법, {}표기법, format표기법 (어제 했을듯?)

# format표기 - dictionary
subject_dic = {'python' : 'kim', 'c++' : 'sung', 'data structure' : 'kim', 'database' : 'kang'}
print("{0[python]} {0[data structure]}".format(subject_dic))

# 5장 끝부분 과제 풀어보기





# chapter 6
# 반복문
# while문

# 소수인지 판별
number = int(input("Input number : "))
cnt = 0;
i = 2
while i < number :
    if number % i == 0 :
        cnt += 1
        break
    i += 1
if cnt == 0 :
    print(f'{number} is prime number')
else :
    print(f'{number} is not prime number')