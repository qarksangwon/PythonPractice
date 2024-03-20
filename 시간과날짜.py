from datetime import datetime # datetime 모듈의 datetime 함수를 가져 옴.
import calendar

print(datetime.today().month)   #월
print(datetime.today().day)     #일
print(datetime.today().hour)    #시
print(datetime.today().minute)  #분
print(datetime.today().second)  #초

print(calendar.calendar(2023))
print(calendar.calendar(2023, m=4))     # 4열로 표시
print(calendar.month(2023, 10))    # 지정 년도 지정 월 표시
print(calendar.monthrange(2023,10))      # 시작 요일과 총 일수 반환
# 요일은  월 화 수 목 금 토 일 -> 0 1 2 3 4 5 6  월 부터 일, 0 부터 6

