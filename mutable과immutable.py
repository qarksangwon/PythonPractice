# Mutable
# 객체의 값 수정 가능
# 새로운 객체 생성 가능
# list, dictionary, class 객체
# Call - By - Reference (참조 타입)

a = [1,2,3,4]
b = a
print(id(a),id(b))
a.append(-1)
print(a,b) # 즉, 참조 타입 = 같은 곳을 참조, 한곳에 추가 시 같이 변동
print(id(a),id(b))

# slicing 은 새로운 객체를 생성
a = a[:] + [5]
print(a,b) # 그렇기 때문에 이는 같은 객체를 참조 안함


# Immutable
# 객체의 값을 수정할 수 없음
# 수정, 즉 연산을 수행할 시 새로운 객체가 생성됨
# 예외 케이스 있음(연산 결과가 동일, immutable 내에 mutable element 존재)
# int, float, str, tuple
# Call - By - Value
a = 1
b = a
a += 1
print(a,b)
# 예외 케이스 중 결과가 동일할 때는 같은 주소를 가리키는 것
x = 'abcd'
y = x
print(id(x), id(y))
# 하지만 값이 변경된다면?
x +='e'
print(x, y)
print(id(x), id(y))

# 즉, Immutable 은 값을 변경 할 수 없다. 새로운 값이 생성 되는 것
# 하지만 Mutable 은 값을 변경 할 수 있다는 것.
