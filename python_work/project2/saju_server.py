from flask import Flask, request, jsonify
import json

import LuckCrawler as LC

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process_post_request():
    try:
        data = request.get_json()
        # 여기에서 데이터를 처리하고 응답을 생성합니다.
        json_result = LC.TranceLuckData(data)
        # JSON 파일로 저장
        json_data = json.dumps(json_result, ensure_ascii=False)
        json_variable = json_data
        # 이 예제에서는 받은 데이터를 그대로 반환합니다.
        return jsonify(json_variable)
    except Exception as e:
        return str(e), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
