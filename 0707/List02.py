# 동시에 두 개 이상의 리스트를 반복하기 위한 zip() 함수

questions = ['name', 'quest', 'color']
answers = ['kim', '파이썬', 'blue']

for q, a in zip(questions, answers) :
    print(f"What is your {q}? It is {a}")