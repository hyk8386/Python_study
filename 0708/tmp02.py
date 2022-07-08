# 리스트 추가 방법에 따른 시간 테스트
import time

SIZE = 50000

start_time = time.time() # 현재시간
myList = []
for i in range(SIZE):  # 5만번 돌림
    myList = myList + [i*i]
print("수행시간=", time.time() - start_time)
# 대입연산자 사용 - 하나의 값이 들어올 때마다 재설정


start_time = time.time()  # 현재시간 초기화
myList = []
for i in range(SIZE):
    myList.append(i*i)
print("수행시간=", time.time() - start_time)
# append 사용 - 단순히 추가
