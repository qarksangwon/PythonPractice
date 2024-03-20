# 리스트 []: 연속적으로 저장 되는 자료형, 크기 동적 할당
# 여러 타입 섞어서 넣을 수 있다.
# 리스트 내 리스트 가능
# 읽기, 쓰기 가능
num = [1, 2, 3, 4, 5, 6, 7]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'apple', True, 3.14 , ['ev6', 'grandeur', 'genesis']]
print(fruits[1][2])  # str 은 배열 개념
print(mixed[4][2])
print(mixed[4][2][5])

print(str(mixed[3])[1])

# 변수와 리스트 비교
kor, eng, mat = 80, 75, 90
total = kor + eng + mat
print(total/3)

score = [80, 75, 90]
print(sum(score)/len(score))

new_list = [1, 2, 3]
new_list.append(4) # 뒤에 붙임
new_list.append(5)

new_list.insert(1, 999) # index, 자리에 value 넣기
print(new_list)

# 맨뒤 반환 뒤 삭제, stack 의 pop 과 같은 기능 인듯
print(new_list.pop())   # 반환은 됐으니 이후 pop 된 list 임
print(new_list)

new_list.pop(2)  # index 2 값 삭제
print(new_list)

new_list.remove(999)   # 값을 제거
print(new_list)

del new_list[2] # index 2 값 삭제
print(new_list)

new_list.clear()      # 전체 삭제
print(new_list)

# 중복 제거
# 리스트 순회 (for 문으로) 하면서 not in 혹은 in 을 사용.
my_list = ['a','b','c','d','a','e','b','f']
onlyOne_list = []
for e in my_list:
    if e not in onlyOne_list: onlyOne_list.append(e)
print(onlyOne_list)





    