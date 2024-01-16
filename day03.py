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
number1 = input("First Number : ")
number2 = input("Second Number : ")
print(number1 + number2) # int로 형변환하지 않아 문자열 결합

