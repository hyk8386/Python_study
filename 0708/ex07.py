# 튜플 / 딕셔너리 / 셋

# tuple - 변경 불가 - ( )
fruits = ("apple", "banana", "grape")
print(fruits)
print(fruits[0])
for f in fruits:
    print(f, end=" ")

# tuple을 리스트로 -> 튜플은 내용이 수정이 안되기 때문에 수정할 경우 리스트로 바꿈
myTuple = (1, 2, 3, 4)
myList = list(myTuple)
print()
print(myList)


# dictionary - key/value - { }


# set - 중복 불가 - { }
numbers = {1, 2, 3}
print("set=", numbers)

numbers = set([1, 2, 2, 3, 4, 5, 5]) # 중복 불허
print("set=", numbers)

# set 함축 연산
aList = [1, 2, 3, 4, 5, 1, 2]
result = {x for x in aList if x % 2 == 0}
print("x=%2", result)

# set - 교집합 / 합집합 / 차집합
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "kiwi"}
C = A & B
D = A | B
E = A - B
print("교집합", C)
print("합집합", D)
print("차집합", E)
