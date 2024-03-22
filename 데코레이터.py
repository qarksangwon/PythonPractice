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
test = datetime_deco(for_sum)
test()

# 방법 2
for_sum()