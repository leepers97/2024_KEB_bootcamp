# 단순 연결리스트
# ## 클래스와 함수 선언 부분 ##
# class Node() :
# 	def __init__ (self) :
# 		self.data = None
# 		self.link = None
#
# def printNodes(start) :
# 	current = start
# 	if current == None :
# 		return
# 	print(current.data, end = ' ')
# 	while current.link != None:
# 		current = current.link
# 		print(current.data, end = ' ')
# 	print()
#
# def makeSimpleLinkedList(namePhone) :
# 	global memory, head, current, pre
# 	printNodes(head)
#
# 	node = Node()
# 	node.data = namePhone
# 	memory.append(node)
# 	if head == None :			# 첫 번째 노드일 때
# 		head = node
# 		return
#
# 	if head.data[1] > namePhone[1] :	# 첫 번째 노드보다 작을 때
# 		node.link = head
# 		head = node
# 		return
#
# 	# 중간 노드로 삽입하는 경우
# 	current = head
# 	while current.link != None :
# 		pre = current
# 		current = current.link
# 		if current.data[1] > namePhone[1]:
# 			pre.link = node
# 			node.link = current
# 			return
#
# 	# 삽입하는 노드가 가장 큰 경우
# 	current.link = node
#
# ## 전역 변수 선언 부분 ##
# memory = []
# head, current, pre = None, None, None
# dataArray = [["지민", "180"], ["정국", "177"], ["뷔", "183"], ["슈가", "175"], ["진", "179"]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#
# 	for data in dataArray :
# 		makeSimpleLinkedList(data)
#
# 	printNodes(head)




# 원형 연결 리스트
# 첫 번째 노드 삽입 쪽이 핵심
# 아래는 단순 연결 리스트 삭제 코드 -> 원형 연결 리스트 삭제 코드로 바꿔보기

## 클래스와 함수 선언 부분 ##
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def deleteNode(deleteData) :
	global memory, head, current, pre

	if head.data == deleteData :         # 첫 번째 노드 삭제
		current = head
		head = head.link
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

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	printNodes(head)

	deleteNode("다현")
	printNodes(head)

	deleteNode("쯔위")
	printNodes(head)

	deleteNode("지효")
	printNodes(head)

	deleteNode("재남")
	printNodes(head)



# 1 - 4 45p
import random
# arr = [random.randint(1, 100) for i in range(7)]
# for i in arr :
#     print(i)


# self study 5 - 2
# arr2 = [random.randint(-100, 100) for i in range(7)]
# for i in arr2 :
#     print(i)
#
# for i in arr2 :
# 	i *= -1
# 	print(i)




# 스택




# 이진트리
# class TreeNode() :
# 	def __init__ (self) :
# 		self.left = None
# 		self.data = None
# 		self.right = None
#
# node1 = TreeNode()
# node1.data = '화사'
#
# node2 = TreeNode()
# node2.data = '솔라'
# node1.left = node2
#
# node3 = TreeNode()
# node3.data = '문별'
# node1.right = node3
#
# node4 = TreeNode()
# node4.data = '휘인'
# node2.left = node4
#
# node5 = TreeNode()
# node5.data = '쯔위'
# node2.right = node5
#
# node6 = TreeNode()
# node6.data = '선미'
# node3.left = node6
#
# node7 = TreeNode()
# node7.data = '다현'
# node4.right = node7
#
# node8 = TreeNode()
# node8.data = '사나'
# node6.right = node8
#
# def preorder(node) :
# 	if node == None:
# 		return
# 	print(node.data, end='->')
# 	preorder(node.left)
# 	preorder(node.right)
#
# def inorder(node):
# 	if node == None :
# 		return
# 	inorder(node.left)
# 	print(node.data, end='->')
# 	inorder(node.right)
#
# def postorder(node):
# 	if node == None :
# 		return
# 	postorder(node.left)
# 	postorder(node.right)
# 	print(node.data, end='->')
#
# print('전위 순회 : ', end = '')
# preorder(node1)
# print('끝')
#
# print('중위 순회 : ', end = '')
# inorder(node1)
# print('끝')
#
# print('후위 순회 : ', end = '')
# postorder(node1)
# print('끝')



## 함수 선언 부분 ##
class TreeNode() :
	def __init__ (self) :
		self.left = None
		self.data = None
		self.right = None

## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크',  '걸스데이', '트와이스', '잇지', '여자친구' ]

## 메인 코드 부분 ##
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :

	node = TreeNode()
	node.data = name

	current = root
	while True :
		if name < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right

	memory.append(node)

findName = input("찾을 그룹이름--> ")

current = root
while True :
	if findName == current.data:
		print(findName, '을(를) 찾음.')
		break
	elif findName < current.data :
		if current.left == None :
			print(findName, '이(가) 트리에 없음')
			break
		current = current.left
	else :
		if current.right == None :
			print(findName, '이(가) 트리에 없음')
			break
		current = current.right

# 선형 리스트, 단순 연결 리스트, 원형 연결 리스트, 스택, 큐
# 마지막쪽 연습문제(10문제..?)