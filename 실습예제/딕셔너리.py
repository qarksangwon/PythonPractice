# 키를 통해 값에 접근하는 방식
# 자바의 map 과 같음

dict = {"박재훈":100, "범스테드":100, "데릭":100, "로니콜먼":120}
# 값 불러올 때 get() 함수 혹은 [key] 로 가능
print(dict["박재훈"])
print(dict.get("박재훈"))

# 딕셔너리 정보 가져오기
print(dict.keys())
print(dict.values())
print(dict.items())

# 한 번에 수정
dict.update({"박재훈":200, "로니콜먼":200})
print(dict)


# 딕셔너리 에서도 in 사용으로 해당 키 값 여부 확인 가능
print("박재훈" in dict)
print(100 in dict) # 키 값으로 확인해야함

