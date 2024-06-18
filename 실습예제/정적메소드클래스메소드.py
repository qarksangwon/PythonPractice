# 정적 메소드
# 클래스 내에 두긴 하지만, 인스턴스와는 무관하게 독립적으로 동작하는 함수
# 인자로 self를 사용하지 않고, 해당 정적 메서드는 인스턴스 변수나 메서드에 접근 못함.
# 클래스 메소드
# 클래스 변수를 사용하기 위한 함수, 비슷하지만 매개변수로
# 클래스를 넘겨받는 인자가 필요하며, 이를 이용해 클래스 변수에 접근한다.
# 파이썬은 클래스 내에 변수를 선언하면 어디서든 접근 가능한 듯 하다.

class Car :
    isinstance_count = 0

    # 초기화 함수
    def __init__(self, size, model):
        self.speed = None
        self.size = size   # 인스턴스 변수 생성 및 초기화
        self.model = model
        Car.isinstance_count += 1 # 클래스 변수 이용
        print(f"자동차 객체 생성 수 : {Car.isinstance_count}")

    def move(self, speed):
        self.speed = speed
        print(f"자동차 {self.size} & {self.model}가 시속 {self.speed}로 달립니다.")

    @staticmethod
    def check_type(code):
        if(code >= 10): print("전기차 입니다.")
        elif(code >= 20): print("가솔린차 입니다.")
        elif(code >= 30): print("디젤차 입니다.")
        else: print("분류 코드가 없습니다.")

    @classmethod
    def print_count(cls):
        print(f"{cls.isinstance_count} 개의 차량.")

car1 = Car("소형", "모닝")
car2 = Car("중형", "쏘나타")

car1.move(90)
Car.check_type(11)
car2.move(70)
Car.print_count()
print(car1.isinstance_count)
print(car2.isinstance_count)