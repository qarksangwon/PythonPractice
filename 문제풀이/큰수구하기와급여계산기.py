# 3자의 정수 입력 받고 각 자리 수 중 큰 수 구하기
# val = int(input("세자리 입력 : "))
# hundredVal = val//100
# tenVal = (val%100)//10
# oneVal = val%10
# value = [hundredVal,tenVal,oneVal]
# print(max(value))
test = []
for val in input("세자리 입력 : "):
    test.append(val)
print(max(test))


# 주/야간 근무시간 입력 받아 급여 계산
# 주간 : 9620 원 / 야간 : 주간 시급 * 1.5
isWeekly = int(input("주간근무[1] 야간근무[2] 입력 : "))
time = int(input("근무 시간 입력 : "))
if isWeekly == 1:
    salary = 9620 * time
else :
    salary = 9620*1.5*time
type = isWeekly==1 and "주간" or "야간"
print(f"입력한 시간 동안 근무한 {type} 급여는 {salary}원 입니다.")

