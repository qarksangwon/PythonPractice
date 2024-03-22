# 클로저는 내부 함수(inner function)을 구현하고 그 내부 함수를
# 반환하는 함수를 말한다. 외부 함수는 자신이 가진 변수값 등을
# 내부 함수에 전달해 실행된다고 한다.
# 객체지향 언어에서 생성된 객체 내부의 메소드가 필드를 참조하는 것과 유사한 개념

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a*x +b
    return mul_add

c = calc()
print(calc()(1), c(2), c(3))