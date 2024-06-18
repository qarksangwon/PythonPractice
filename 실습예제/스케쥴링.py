import schedule
import time
import requests
from bs4 import BeautifulSoup

def perform_web_crawling():
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)

def job():
    print("크롤링 시작")
    perform_web_crawling()

# 매일 정해진 시간에 동작
# schedule.every().day.at("18:20").do(job)

# 1분에 한번
# schedule.every(1).minutes.do(job)

# 10초에 한번
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending() # 대기 중인 작업을 수행
    time.sleep(1) # 1초 대기, CPU 사용량 줄이기 위해 사용
