import requests

# 공공 데이터 포털에서 지급 받은 API 키 입력.
# Decoding 된 key 를 사용할 수도 있으니 문서 확인.
# Decoding key 를 바로 넣어서 써도 되지만 requests.utils.unquote()를 통해 바꿀 수 있다.
API_KEY = ''
API_KEY_decode = requests.utils.unquote(API_KEY)
print(API_KEY_decode)