# 파이썬 함수는 반환타입 없이
# def 함수명(매개변수): 로 선언

def recu_sum(a):
    if a==1 : return 1
    else : return recu_sum(a-1)+a

print(recu_sum(10))

# 튜플 ( 수정 불가 ) 은 2개의 리턴값 가질 수 있음
# 내장함수 divmod() <- 몫과 나머지 반환받는 함수랑 같은 원리
def swap_func(a,b):
    temp = a
    a = b
    b = temp
    return (a,b)

a, b = swap_func(10,5)
print(a,b)

# 람다
# def 함수명(매개변수): -> (lambda 매개변수: return할 식)(param1,param2)
def add(a,b):
    return a+b
# 위를 람다식으로 바꾸면
print((lambda a,b : a+b)(1,2))
