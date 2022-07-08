# 리스트 병합, 복제, 비교
# 병합
heroes1 = ["아이언맨", "토르"]
heroes2 = ["헐크", "스칼렛"]

avengers = heroes1 + heroes2
print("병합 : ", avengers)

# 복제
numbers = [1, 2, 3, 4] * 3
print("반복 : ", numbers)

# 비교
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [3, 4, 5, 6]
print("비교 list1==list2", list1==list2)
print("비교 list2==list3", list2==list3)


