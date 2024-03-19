#규칙1 : http://naver.com에서 앞의 http:// 잘라내기
#규칙2 : 처음 만나는 점(.) 이후는 제외
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된
# 'o' 갯수 +글자에 포함된 'k' 갯수+ '!' + 자신의 이니셜(예: 'jks')

file_name = "pwd.txt"
f = open(file_name, "wt")
while True:
    url = input("입력 : ")
    if url == 'q' or url == 'Q' : break
    str1 = url.replace("http://","")
    str1 = str1[:str1.find(".")]
    password = str1[:3] + str(len(str1)) + str(str1.count('o')) + str(str1.count('k')) + '!' + "psw"
    f.write(password+"\n")

f.close()