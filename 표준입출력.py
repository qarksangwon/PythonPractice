print("""동해 물과 백두산이 마르고 닳도록 하느님이
보우 하사 우리 나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한 으로 길이 보전 하세""")

print("파""이""썬")

print('파','이',"썬")

print("\"안녕하세요\" 라고 말했습니다.")

print("서울시 \t 강남구 \t 역삼동 끼얏호우\b\b\b")

print("사과 \r바나나")

# end : 출력 시 끝 문자 지정
# sep : 중간 삽입 문자 지정 :  ',' 로 기본 공백 사용
print("Hello" ,end = "-")
print("World")
print(1,2,3,4,5,6,7,8,9,10)
print(1,2,3,4,5,6,7,8,9,10,sep="-")


print("-"*5,"스타일 지정","-"*5,sep="")
name = "홍길동"
gender = "남성"
age = 25
print("이름 : %s"%name)
print("나이 : %d, 성별 : %s" %(age,gender))

print("이름 : {}".format(name))
print("나이 : {}, 성별 : {}".format(age,gender))

print(f"이름 : {name}")
print(f"나이 : {age}, 성별 : {gender}")

print("이름 : " + name)
print("나이 : " + str(age) + ", 성별 : " + gender)


# map 은 2개의 인자값(매개 변수) 를 가짐
# 첫번 째는 콜백 함수 자리, 즉 데이터 타입
# 두번 째는 입력 값들
# map 의 특징은 입력 받은 데이터를 동일한 개수 만큼 변환해서 반환
score1,score2,score3 = map(int, input("점수1 점수2 점수3 :").split())
print(f"당신이 입력한 점수 : {score1},{score2},{score3}")

name, addr = input("이름과 주소 입력 : ").split() #형변환 필요 없으면 map 필요 없음!
print(f"이름 : {name} , 주소 : {addr}")

list1 = list(map(int,input("성적 모두 되는 대로 입력 : ").split()))
print(list1)

time = list(input("시:분:초 로 입력").split(":"))
print(f"{time[0]} : {time[1]} : {time[2]}")

hour,min,sec = map(int, input("시:분:초").split(":"))
if(hour>12):
    hour -= 12
    print(f"오후{hour:02}시 {min:02}분 {sec:02}초")
else:

    print(f"오전{hour:02}시 {min:02}분 {sec:02}초")