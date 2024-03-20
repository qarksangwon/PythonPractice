# 1~45 로또번호 6개
import random

lotto = []
while True:
    ranVal = random.randint(1, 45) # randrange(1,46)
    if ranVal not in lotto:
        lotto.append(ranVal)
    if len(lotto) == 6 : break
print(lotto)

# 임의의 수 공백으로 입력 받아 홀, 짝수 리스트로 나누어 담기
# 1 2 3 4 5 6 7 8 9 10
# 홀수 : 1 3 5 7 9
# 짝수 : 2 4 6 8 10

inputNum = map(int,input("").split(" "))
evenNum = []
oddNum = []
for e in inputNum:
    if e % 2 == 0 : evenNum.append(e)
    else : oddNum.append(e)
print(f"홀수 : {oddNum}")
print(f"짝수 : {evenNum}")