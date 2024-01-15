# 주석처리 : 컨트롤 + /
# 문자열은 수정 물가능(imutable)
univ = "inha university"
subjects = ["python", "c++", "Linux", "data structure & algorithm", "database"]
print(subjects[1])

# list는 수정 가능(mutable)
subjects[1] = "C++"
print(subjects[1])
