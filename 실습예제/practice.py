print("Hello, Python!")
print(100)
print(100 * 100)

# 파이썬 주석 방식
# 샵 or 따옴표
'''
이것도 주석
'''
"""
이것 또한 주석
"""

name = "이름"
email = "email123"
position = "중립"
addr = "서울시 강남구 역삼동 KH 정보 교육원"
# 따옴표 세 개로 하면 출력 모양을 그대로 만들 수 있음 작은 따옴표 또한 가능
print(f"""
주소 : {addr}
자세 : {position}
이름 : {name}
이메일 : {email}
""")

input_data = input("입력하세요 : ")

if input_data == "홍길동":
    print("당신의 입력값은 홍길동")
else :
    print("아잇 몰라이!")

print(38)  # 숫자 출력
print("문자열 출력")
print([1, 2, 3, 4, 5])  # 리스트 출력
print("|{:5}|".format(10))
print(f"|{10:5}|")