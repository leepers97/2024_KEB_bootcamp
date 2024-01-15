# 예습 문제
# 섭씨 화씨 3번을 누르기 전에는 계속 프로그램이 돌아가게

while True :
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
        print("Wrong Input")