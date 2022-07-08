# dictionary - key/value - { }

capitals = {"korea":"Seoul", "USA":"Washington", "UK":"London"}
print(capitals["korea"])
print(capitals["USA"])

for key in capitals:    # 키 출력
    print(key, end=" ")

print()

for key in capitals:    # 값 출력
    print(capitals[key], end=" ")

print()

for key in capitals:    # 키와 값 출력
    print(key, ":", capitals[key], end=", ")

print()
# dictionary 함축
values = [1, 2, 3, 4, 5, 6]
dic = {x : x**2 for x in values if x%2 == 0}
print(dic)