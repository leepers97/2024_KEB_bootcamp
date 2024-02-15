# ## 함수 선언 부분 ##
# import random
# def findInsertIdx(ary, data) :
# 	findIdx = -1			# 초깃값은 없는 위치로
# 	for i in range(0, len(ary)) :
# 		if (ary[i] > data ) :
# 			findIdx = i
# 			break
# 	if findIdx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
# 		return len(ary)
# 	else :
# 		return findIdx
#
# ## 전역 변수 선언 부분 ##
# before = [random.randint(0, 200) for _ in range(10)]
# after = []
#
# ## 메인 코드 부분 ##
# print('정렬 전 -->', before)
# for i in range(len(before)) :
# 	data = before[i]
# 	insPos = findInsertIdx(after, data)
# 	after.insert(insPos, data)
# print('정렬 후 -->', after)

# 선택정렬 연습
# def Find_min(arr) :
#     min_num = arr[0]
#     for i in arr :
#         if i <= min_num :
#             min_num = i
#     return min_num
# def Choice(arr) :
#     min_num = Find_min(arr)
#     for i in arr :
#         if i < min_num :
#
#
# arr1 = [5, 2, 6, 3, 8, 9, 1]
# Choice(arr1)


## 함수 선언 부분 ##
def quickSort(ary):
    n = len(ary)
    if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n // 2]  # 기준값을 중간값으로 지정
    leftAry, rightAry = [], []

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)


## 전역 변수 선언 부분 ##
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)

