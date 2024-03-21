# 튜플은 read_only 즉 한번 선언 뒤 넣거나 수정 불가능
# list 와 같이 index 로 접근할 수 있다.

tp = (1, 1, 2, 2, 2, 3, 3, 3, 3)
print(tp.count(3))  # 데이터 개수 세기
print(tp.index(3)) # 찾고싶은 데이터가 처음 나오는 index 반환
print(tp[5]) # 해당 index에 있는 값 반환
print(tp.__len__()) # 데이터 개수
print(len(tp))
print(tp.__str__()) # 문자열 형태로 변환 (값)

tp2 = (5,6)
print(tp+tp2)  # 튜플 더하기, 뒤에 붙여짐

# 튜플 자체는 값을 변경하거나 넣거나 삭제할 수 없기 때문에
# 패킹과 언패킹으로 데이터를 관리할 수 있다.
# 패킹 -> 선언 시 () [] {} 생략 시 자동 (), 즉 튜플.
list1 = [10,"열",True]
tuple1 = list1[0],list1[1],list1[2]
print(type(tuple1))
# 언패킹 -> 도로 분해
a, b, c = tuple1
print(a,b,c)
print(type(a),type(b),type(c))

# 집합 : set() -> 중복 제거시 활용, java 의 set 과 같음
# 순서 없음, 고유값 가짐, 중복 불가능, mutable 특성 가짐
# mutable : 수정 가능, 새로운 객체 생성 가능, => list, dictionary, set
# immutable : 수정 불가, 객체 값으로 연산 수행 시 새로운 객체 생성, 예외 존재 => tuple, string, int...기본자료형
# set([]) 자체를 {} 로 생략 가능, 딕셔너리도 {} 이지만 : 을 사용해
# 키값을 나눈다는 점에서 다름,
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
s3 = {1, 2, 3, 4, 5, 6, 2, 3, 4, 5}
print(s3)
print(type(s3))


# 이름과 같이 set -> 수학의 집합의 역할 가능
# 교집합
print(s1.intersection(s2))

# 합집합
print(s1.union(s2))

# 차집합
print(s1.difference(s2))