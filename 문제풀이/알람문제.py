# 첫 줄에 시간과 분 입력
# 입력은 24시간 표기
# 45분 빠르게 출력

H,M = map(int,input().split(" "))
if M < 45:
    H = H-1
    M  = M+15
else:
    M = M-45

print(str(H)+":"+str(M))