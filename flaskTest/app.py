from flask import Flask
from routes.data import get_data
from routes.weather import get_weather, get_weather2
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

app.add_url_rule('/api/data', 'get_data', get_data, methods=['GET'])
app.add_url_rule('/api/weather', 'get_weather', get_weather, methods=['GET'])
app.add_url_rule('/api/weather2','get_weather2', get_weather2, methods=['GET'])

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)