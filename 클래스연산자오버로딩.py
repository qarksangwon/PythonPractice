# 연산자 오버로딩은 내장 연산자를 재정의 해서 클래스에 대해 다르게 동작하게 함
# __add__(self,other)  : 덧셈
# __sub__(self, other) : 뺄셈
# __mul__(self, other) : 곱셈
# __div__(self, other) : 나눗셈
# __eq__(self, other) : equal
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def infoView(self):
        return print(f"x : {self.x}, y : {self.y}")


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

v3 = v1 + v2  # '+' 연산자가 __add__ 메서드를 호출합니다.
print(v3.infoView())
print(v1 == v2)  # '==' 연산자가 __eq__ 메서드를 호출합니다.
