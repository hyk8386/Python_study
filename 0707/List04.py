# 리스트의 탐색과 삭제

# 탐색
heroes = ["아이언맨", "토르", "헐크", "스칼렛", "토르"]
n = heroes.index("헐크")
print(n)

# 삭제
heroes = ["아이언맨", "토르", "헐크"]
h = heroes.pop(1) # pop은 인덱스 값으로 삭제
print(heroes)

heroes = ["아이언맨", "토르", "헐크"]
h = heroes.remove("토르") # remove는 데이터로 삭제
print(heroes)