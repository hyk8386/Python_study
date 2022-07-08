# 슬라이스 응용
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white', 'blue', 'red']
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[::2] = [99, 99, 99, 99]
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = [ ]
print(lst)

# 출력식 : 입력리스트
squares = [x * x for x in range(10)] # for문 - 0~9까지 / x*x 계산
print("=>", squares)

# 출력식 : 입력리스트 : 조건식
squares = [x * x for x in range(10) if x %2 == 0] # for문 - 0~9까지 / x*x 계산 / 2로 나눈 나머지가 0인 수
print("%2=>", squares)