import random

for i in range(2,5):
    print(i, end=" ")
print()

for i in range(random.randrange(5)):
    print(i, end =" ")
print()

n = int(input("숫자 입력: "))
#
# for i in range(1,n+1,2):
#     print(i,end=" ")

# sum = 0
# while n: # 정수에서 0이 아니면 True, 0은 False
#     sum += n
#     n -= 1
# print(sum)


# while True:
#     age = int(input("나이 입력:"))
#     if 0<=age<200 : break # 범위 줄 때 and 나 or 없이 바로 가능
#     print("입력 값 범위 벗어남.")

#별
# 사각형
for i in range(n):
    for j in range(n):
        print("*",end="  ")
    print()

# 점점 많아지거나 적어지거나 오른쪽 정렬
for i in range(n+1):
    print('*'*i)
print()


r = n
for i in range(r+1):
    print("*"*r)
    r = r-1

r = n
for i in range(r+1):
    print(" "*i,end="")
    print("*"*r)
    r = r-1

