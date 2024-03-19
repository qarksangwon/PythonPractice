# kor = int(input("국어 점수 : "))
# eng = int(input("영어 점수 : "))
# mat = int(input("수학 점수 : "))
# avg = (kor+eng+mat)/3
# if avg>=90 : print("A")
# elif avg>=80 :print("B")
# elif avg>=70 : print("C")
# elif avg>=60 : print("D")
# else : print("F")

id = input("ID 입력 : ")
if len(id) >= 10:
    pw = input("Password 입력 : ")
    if len(pw) < 8 or len(pw) > 16:
        print("Password 는 8자 이상 16자 이하로 입력 바랍니다.")
    elif pw.find(id) > 0 :
        print("Password 는 ID 를 포함할 수 없습니다.")
    else :
        print(f"ID : {id}  Password : {pw}")
else:
    print("ID 는 10자 이상이어야 합니다.")