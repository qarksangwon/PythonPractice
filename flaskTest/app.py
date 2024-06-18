from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
import requests
import json

app = Flask(__name__)

# 임의의 데이터, 실제 구현에서는 이 부분에 데이터베이스에서 가져온 데이터나
# 계산된 결과를 넣습니다.
data = {
    'stations': ['강남역', '역삼역', '서울역'],
    'ridership': [1000, 800, 1200]
}

# 기본적인 GET 요청을 처리하는 라우트
@app.route('/api/data', methods=['GET'])
def get_data():
    response = Response(
        json.dumps(data, ensure_ascii=False),  # ensure_ascii=False를 설정하여 JSON에 유니코드 문자 포함
        mimetype='application/json; charset=utf-8'  # charset=utf-8을 명시적으로 설정
    )
    return response

@app.route('/api/weather', methods=['GET'])
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"

    return output

@app.route('/api/query', methods=['get'])
def get_query():
    output=""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<{item_type} style='color : {item_color}'>item_color</{item_type}>"
    return output

@app.route('/api/item/<item_id>', methods=['GET'])
def get_path_item(item_id):
    output = ""
    path_item = item_id
    output += f"<h1>{path_item}</h1>"
    return output

@app.route('/api/register', methods=['POST'])
def post_register():
    data = request.get_json()
    username = data.get('username', None)  # .get 메소드를 사용하여 기본값을 None으로 설정합니다.
    password = data.get('password', None)
    return jsonify({"username": username, "password": password})

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)