# import math : 기본 모듈 불러오는 방식
# from math import sin, cos, tan, floor, ceil : 모듈에서 일부분만 불러오기 -> from ~ import ~
import math as m # 불러와서 간단한 약어로 쓰기 -> import ~ as ~
print(m.sin(1))

# sys : 시스템과 관련된 정보를 가지고 있는 모듈
import sys
print("명령 줄 인수 :", sys.argv)
print("실행 경로 :", sys.path[0])
sys.stdout.write("표준 출력")
sys.stderr.write("표준 에러 출력")
# sys.exit(0) # 프로그램 종료

# os : 운영체제와 상호작용 하기 위한 기능
import os

cwd = os.getcwd() # 현재 작업 디렉토리
print("현 작업 디렉토리 :", cwd)

if not os.path.isdir("../testdir"):
    os.mkdir("../testdir") # 디렉토리 생성
print(os.path.isfile("score.txt")) # 파일 여부 확인
print(os.path.isdir("../testdir")) # 디렉토리 여부 확인
# os.system("pwd") # 시스템 명령 실행

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password

# 진입 지점을 지정해서 현재 파일에서 실행시키면 실행되는 코드
# 특수한 상황에 부여하기 좋아 보임.
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))