import requests
import json

data = {
    "id" : "ID1234",
    "pwd" : "pwd1234"
}

url = "http://localhost:8111/login"
headers = {"Content-Type":"application/json"}

response = requests.post(url, data=json.dumps(data), headers = headers)

if(response.status_code == 200):
    print("데이터 전송 성공")
else:
    print("데이터 전송 실패 [", response.status_code,"]")