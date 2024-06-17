import requests
from bs4 import BeautifulSoup
res = requests.get("http://naver.com")
print("응답 코드 ",res.status_code)

if res.status_code == 200 :
    soup = BeautifulSoup(res.text, "lxml")
    print(soup.find({"class":"notify_area"}))
else:
    print("실패")