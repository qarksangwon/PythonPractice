# try except else finally로 사용
# try -> 예외 발생할 구문
# except -> 예외 발생시 실행 구문
# else -> 예외 발생하지 않을 때 실행할 구문
# finally -> 무조건 실행

try:
    print("나눗셈")
    num1 = int(input("첫 수 : "))
    num2 = int(input("두번 째 수 : "))
    print(f"{num1}/{num2} = {int(num1/num2)}")
except ValueError:
    print("값을 제대로 넣으시오!")
except ZeroDivisionError as err: # 0으로 나눌 때
    print(err)
except Exception as err :
    print(err)
else:
    print("출력 잘~ 했다!")
finally:
    print("종료합니다 . . . ")