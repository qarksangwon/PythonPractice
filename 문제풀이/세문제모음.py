# 3개 정수 입력 받아 최대 최소 구함
list1 = input("세 정수 입력 : ").split()
print(f"최대 : {max(list1)} 최소 : {min(list1)}")
print()

# 주민등록번호 입력 받아 생년월일, 성별, 나이 출력
jm = input("주민등록번호 입력 (-포함): ")
gen = ""
if jm[7] == "1" or jm[7] == "3" : gen = "남성"
else : gen ="여성"
yy = int(jm[:2])
age = 0
if 24>yy: age=24-yy
else : age = 100-yy+24
print(f"""생년월일 : {jm[0:2]}년 {jm[2:4]}월 {jm[4:6]}일
성별 : {gen}
나이 : {age}""")
print()

# 2개의 문자열 S 와 K , 정수 N 을 입력받아 S의 뒷 부분의 N을 가져와서 합쳐서 출력
# 예)    s:seoul
#        k:korea
#        n:2  -> result : ulkorea

s, k, N = map(str,input("세 문자 입력 : ").split())
n = int(N)
s = s[-n:]
print(s+k)