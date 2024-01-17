# 과제
# 1. 영어-프랑스어 사전을 의미하는 e2f 딕셔너리를 만들어 출력해보자. 영어 dog는 프랑스어 chien이고 cat은 chat, walrus는 morse다
e2f_dic = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}
print(f'1. {e2f_dic}')

# 2. e2f 딕셔너리에서 영어 walrus를 프랑스어로 출력해보자
print(f'2. {e2f_dic["walrus"]}')

# 3. e2f 딕셔너리에서 f2e 딕셔너리라는 영어-프랑스어 사전을 만들어보자(item 메서드 사용)
f2e = e2f_dic.items()
print(f'3. {f2e}')

# 4. e2f 딕셔너리를 사용해서 프랑스어 chien을 영어로 출력해보자
print(f'4. {e2f_dic["dog"]}')

# 5. e2f 딕셔너리의 영어 단어 키들을 출력해보자
print(f'5. {e2f_dic.keys()}')

# 6. 이차원 딕셔너리 life를 만들어보자. 최상위 키는 'animals', 'plants', 'others'다. 그리고 'animals'는 각각 'cats', 'octopi', 'emus'를 키로 하고,
#    'Henri', 'Grumpy', 'Lucy'를 값으로 하는 또 다른 딕셔너리를 참조하고 있다. 나머지 요소는 빈 딕셔너리를 참조한다.
life = {
    'animals' : dict(cats = "Henri", octopi = "grumpy", emus = "Lucy"),
    'plants' : dict(),
    'others' : dict()
}

# 7. life 딕셔너리의 최상위 키를 출력해보자
print(f'7. {life.keys()}')

# 8. life['animals']의 모든 키를 출력해보자
print(f'8. {life["animals"].keys()}')

# 9. life['animals']['cats']의 모든 값을 출력해보자
print(f'9. {life["animals"]["cats"]}')

# 10. 딕셔너리 컴프리헨션으로 squares딕셔너리를 생성한다. range(10)을 키로 하고, 각 키의 제곱을 값으로 한다
# num = []
# for i in range(10):
#     num.append(i)
# sqaures = {ans : ans**ans for ans in num}
sqaures = {ans : ans**ans for ans in range(10)}
print(f'10. {sqaures}')

# 연습
dic = {'aaa' : 111, 'bbb' : 222}
#print(dic)
dic['ccc'] = 333
#print(dic)
# dic['ccc'] = 222
print(dic)
for aa, bb in dic.items() :
    print(f'첫번째는 {aa}, 두번째는 {bb} 입니다')