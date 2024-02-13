# 선형리스트
# 1.
# def Add_list(list, new_info) :
#     is_big = False
#     for i in range(len(list)) :
#         # 반복문 돌면서 new_info[1]이 list[1]보다 크거나 같다면
#         if new_info[1] >= list[i][1] :
#             # 그 순서부터 한 칸씩 밀고
#             list[i + 1] = list[i]
#             # 그 순서에 new_info 삽입
#             list[i] = new_info
#             is_big = True
#             break
#     # 더 큰 수가 없다면
#     if is_big == False :
#         # 맨 뒤에 삽입
#         list.append(new_info)
#     for i in list :
#         print(i)
#
# friend_list = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
# while True :
#     new_friend = input("추가할 친구--> ")
#     num = int(input("카톡 횟수--> "))
#
#     new_info = (new_friend, num)
#
#     Add_list(friend_list, new_info)



# 2.
## 함수 선언 부분 ##
def printPoly(arr):
    polyStr = "P(x) = "

    for i in range(len(arr[0])):
        term = arr[0][i]  # 항 차수
        coef = arr[1][i]  # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xVal, arr):
    retValue = 0

    for i in range(len(arr[0])):
        term = arr[0][i]  # 항 차수
        coef = arr[1][i]  # 계수
        retValue += coef * xValue ** term

    return retValue


## 전역 변수 선언 부분 ##
arr = [[300, 20, 0],
       [7, -4, 5]]

## 메인 코드 부분 ##
if __name__ == "__main__":
    # pStr = printPoly(tx, px)
    pStr = printPoly(arr)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, arr)
    print(pxValue)
