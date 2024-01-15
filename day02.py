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





# chapter 3
# 숫자

# Bool : 0이 아닌 수는 모두 True

# 콤마 사용 X (튜플로 인식)
money = 5,000,000
print(type(money))

cash = 5_000_000 # _로 하면 가능
print(type(cash))



# # 거듭제곱
# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number : '))
# # 1. f스트링
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')
#
# # 2. format 함수
# print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
# print('밑은 {}, 지수는 {}, 결과 값은 {}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
#
# # 3. c like
# print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_number, exponent_number, pow(base_number, exponent_number)))



# # 몫, 나머지 한번에 튜플로
# first_number = int(input("First number : "))
# second_number = int(input("Second number : "))
#
# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'몫은 {quotient} 나머지는 {remainder}입니다')
# print(f'몫은 {divmod(first_number, second_number)[0]} 나머지는 {divmod(first_number, second_number)[1]}입니다')



# 다시 보자 +-
print(-5 ** 2)
print(-(5 ** 2))
print((-5) ** 2)

# 접두어 (다시보자 - 아스키코드 관련, 각각 몇진수인지)
dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec, octal, hexadecimal, binary)
print(chr(binary), chr(octal), chr(hexadecimal), chr(binary)) # 아스키 코드로 변환
print(bin(binary), bin(octal), bin(hexadecimal), chr(binary)) # 이진수로 변환
print(ord('B'), ord('Z'), ord('a'), ord('2')) # 66, 90, 97, 50
# 아스키코드 스타트지점들 외워두기



# # 형변환
# fahrenheit = float(input("Input Fahrenheit : "))
# print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5 / 9) : .4f}C')



print(int('10', 2)) # 2진수
print(int('10', 8)) # 8진수
print(int('10', 16)) # 16진수
print(int('11', 16)) # 16진수
print(int('1A', 16)) # 16진수
print(int('10', 22)) # 22진수





# chapter 4

# menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
# if menu == '1' :
#     fahrenheit = float(input("Input Fahrenheit : "))
#     print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5 / 9) : .4f}C')
# elif menu == '2' :
#     celsius = float(input("Input Celsius : "))
#     print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9 / 5) + 32) : .4f}C')
# else :
#     print("Terminate Program")



# 줄바꿈
sum = 1 + \
    + 2 \
    + 3
print(sum)



# None
temp = []
if temp :
    print("원소가 존재하는 리스트")
else:
    print("비어있는 리스트")



# 모음 자음
letter = input('Input alphabet letter : ')

# set 사용
# vowels = {'a', 'e', 'i', 'o', 'u'}

# 문자열 사용
vowels = "aeiuo"
if letter in vowels :
    print(f'{letter} is a vowel')
else :
    print(f'{letter} is a consonant')