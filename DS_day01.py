# 선형 자료구조 : 리스트, 스택, 큐
# 비선형 자료구조 : 트리, 그래프

import my_math
import time
# 재귀함수는 스택과 메모리를 사용해 느림
# 반복문은 레지스터 내에서 해결
# 속도 빠른 순 : 레지스터 -> 캐시 -> 렘 ...
def factorial(number) -> int :
    # if number < 0 :
    #     return None
    # elif number == 0 or number == 1 :
    #     return 1
    # else :
    #     return number * factorial(number - 1)
    #
    if number == 1 :
        return 1
    else :
        return number * factorial(number - 1)


def timer(func) :
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()
        print(f"소요시간 : {end - start}")
        return result
    return wrapper

# 단일책임원칙(SRP), OCP 위배 : 함수 안에서 시간을 재고 있음
# 데코레이터로 하면 됨
# @timer
# def nCr(n, r) -> int :
#     '''
#     조합함수
#     :param n:
#     :param r:
#     :return:
#     '''
#     numerater = factorial(n)
#     denominator = factorial(n - r) * factorial(r)
#     return int(numerater / denominator)
#
# if __name__ == "__main__" :
#     n = int(input("Input n : "))
#     r = int(input("Input r : "))
#     print(f"{n}C{r} = {my_math.nCr(n, r)}")



# import random
# random_num = random.randint(1, 100)
# cnt = 0
# while True :
#     num = int(input(f"수를 입력하세요 : "))
#     cnt += 1
#     if num == random_num:
#         print(f"정답입니다! {cnt}회 만에 맞추셨습니다!")
#         break
#     else :
#         print("오답입니다")
#         if num > random_num :
#             print("더 작은 수를 입력하세요")
#         elif num < random_num :
#             print("더 큰 수를 입력하세요")



# 선형리스트
# 삽입, 삭제 불리 -> 오버헤드가 많이 생김
## 함수 선언 부분 ##
# def printPoly(p_x):
#     term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1
#     polyStr = "P(x) = "
# 
#     for i in range(len(px)):
#         coef = p_x[i]  # 계수
# 
#         if (coef >= 0):
#             polyStr += "+"
#         polyStr += str(coef) + "x^" + str(term) + " "
#         term -= 1
# 
#     return polyStr
# 
# 
# def calcPoly(xVal, p_x):
#     retValue = 0
#     term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1
# 
#     for i in range(len(px)):
#         coef = p_x[i]  # 계수
#         retValue += coef * xValue ** term
#         term -= 1
# 
#     return retValue
# 
# 
# ## 전역 변수 선언 부분 ##
# px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0
# 
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#     pStr = printPoly(px)
#     print(pStr)
# 
#     xValue = int(input("X 값-->"))
# 
#     pxValue = calcPoly(xValue, px)
#     print(pxValue)




# 연결리스트
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current is None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insertNode(findData, insertData) :
	global head, current, pre
	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		# 아래 두 줄이 핵심
		node.link = head
		head = node
		return

	current = head
	while current.link is not None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node

def deleteNode(deleteData) :
	global memory, head, current, pre

	if head.data == deleteData :         # 첫 번째 노드 삭제
		current = head
		head = head.link
		print(f"{deleteData}가 삭제됨")
		del(current)
		return

	current = head                          # 첫 번째  외 노드 삭제
	while current.link != None :
		pre = current
		current = current.link
		if current.data == deleteData :
			pre.link = current.link
			del(current)
			return
	print(f"{deleteData}가 삭제될 수 없음")

def findNode(findData) :
	global memory, head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != None :
		current = current.link
		if current.data == findData :
			return current
	return Node()	# 빈 노드 반환


## 전역 변수 선언 부분 ##
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	# memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		# memory.append(node)

	printNodes(head)

	insertNode("다현", "화사")
	deleteNode("정연")
	findNode("쯔위")

