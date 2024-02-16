# 이진트리




# 그래프
# dfs
## 클래스 및 함수 선언 부분 ##
# class Graph() :
# 	def __init__ (self, size) :
# 		self.SIZE = size
# 		self.graph = [[0 for _ in range(size)] for _ in range(size)]
#
# ## 전역 변수 선언 부분 ##
# G1 = None
# stack = []
# visitedAry = []		# 방문한 정점
#
# ## 메인 코드 부분 ##
# G1 = Graph(4)
# G1.graph[0][2] = 1; G1.graph[0][3] = 1
# G1.graph[1][2] = 1
# G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
# G1.graph[3][0] = 1; G1.graph[3][2] = 1
#
# print('## G1 무방향 그래프 ##')
# for row in range(4) :
# 	for col in range(4) :
# 		print(G1.graph[row][col], end = ' ')
# 	print()
#
# current = 0		# 시작 정점 A
# stack.append(current)
# visitedAry.append(current)
#
# while (len(stack) != 0) :
# 	next = None
# 	for vertex in range(4) :
# 		if G1.graph[current][vertex] == 1 :
# 			if vertex in visitedAry :  	   # 방문한 적이 있는 정점이면 탈락
# 				pass
# 			else : 			   # 방문한 적이 없으면 다음 정점으로 지정
# 				next = vertex
# 				break
#
# 	if next != None :			  	   # 다음에 방문할 정점이 있는 경우
# 		current = next
# 		stack.append(current)
# 		visitedAry.append(current)
# 	else :            	  	  	  	  # 다음에 방문할 정점이 없는 경우
# 		current = stack.pop()
#
#
# print('방문 순서 -->', end='')
# for i in visitedAry :
# 	print(chr(ord('A')+i), end='   ')





# 재귀
def Recursion(n) :
	if n <= 1 :
		return 1
	return n * Recursion(n - 1)


def Decimal_to_octal(number : int) -> str :
	octal = ''
	while number > 0 :
		octal = str(number % 8) + octal
		number = number // 8
	return octal


def Plus(n) :
	print(n)
	if n <= 1 :
		return 1
	return n + Plus(n - 1)


cnt1 = 0
def Fibo(n) :
	global cnt1
	cnt1 += 1
	a = 0
	b = 1
	for _ in range(n) :
		a, b = b, a + b
	return a



memo = [None for _ in range(100)]
cnt2 = 0
def Fibo_dp(number : int) -> int :
	global memo, cnt2
	cnt2 += 1
	if memo[number] != None :
		return memo[number]
	if number < 2 :
		result = number
	else :
		result = Fibo_dp(number-1) + Fibo_dp(number-2)
		memo[number] = result
	return result


def Prac1(dist, start, end) :
	if start >= end :
		return start
	print(start)
	return Prac1(dist, start + dist, end)

count_dp, count_recu = 0, 0
def recu_fibo(n) :
	global  count_recu
	count_recu += 1
	if n < 2 :
		return 1
	else :
		return recu_fibo(n-1) + recu_fibo(n-2)

# print(Recursion(5))
# print(Decimal_to_octal(10))
# print(Plus(10))
# print(Star(5))
print(Fibo(31))
print(cnt1)
print(Fibo_dp(31))
print(cnt2)


# res = recu_fibo(30)
# print('재귀 방식 --> 답:', res, ', 반복수 : ', count_recu)

# print(Prac1(5, 0, 100))