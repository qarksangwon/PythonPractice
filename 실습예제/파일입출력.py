score_file = open("score.txt", "w", encoding="utf-8") # write 모드는 새로 써짐
# 기존 파일에 덧입력 하고싶다면, "a"
# 한글은 유니코드 체제 -> utf-8

# 내용 넣는 방식은 두가지
print("수학 : 95",file=score_file)
print("영어 : 50",file=score_file)
score_file.write("과학 : 80\n")
score_file.write("국어 : 100\n")
score_file.close()

# 파일은 항상 open -> close 거쳐야 한다. (with 키워드로 생략할 수 있음)

# 파일을 썼으니 읽을 차례
score_file = open("score.txt", "r", encoding="utf-8")

# read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 한 라인씩 읽어 문자열 반환, 파일의 끝(EOF) 에 도달 시 None => "" 반환
# readlines() : 모든 라인을 순서대로 읽어 하나의 요소로 저장하는 리스트 반환

# while True:
#     line = score_file.readline()
#     if not line : break
#     print(line, end="")

lines = score_file.readlines()
print(lines)
for line in lines:
    print(line, end="")

score_file.close()
print()

# with 사용 시 구문이 종료될 때 알아서 close 해줘서 반드시 쓰는걸 강추
with open("score.txt", "r", encoding="utf-8") as score_file:
    lines = score_file.readlines()
    for line in lines:
        print(line, end= "")