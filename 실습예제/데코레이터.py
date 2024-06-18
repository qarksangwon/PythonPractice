# 데코레이터는 이미 만들어진 함수의 앞과 뒤에 기능을 추가하는 것
# 호출 방법은 2개

import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_deco
def for_sum():
    sum = 0
    for i in range(1,100):
        sum += i
    print(sum)

# 방법 1
# test = datetime_deco(for_sum)
# test()
# 이거 두번 찍히는데 이는 datetime_deco 내부에서 func()를 호출할 때 마다,
# 현재 시간을 호출하는데 for_sum()에서 반복문이 여러번 실행돼 반복할 때 decorator 함수가 실행돼서
# 시간이 여러번 찍히는 것이라 한다.

# 방법 2
for_sum()