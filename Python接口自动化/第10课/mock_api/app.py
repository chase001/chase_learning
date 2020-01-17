from flask import Flask, jsonify, request
import time
app = Flask(__name__)


# get 请求方法
@app.route('/', methods=["get"])
def hello_world():
    time.sleep(0.5)
    tmp = None
    try:
        tmp = request.values.get("id")
        print(request.values.get("id"))
    except Exception as e:
        print(e)

    if tmp is None:
        return 'hello world!'
    else:
        return tmp


# post请求方法
@app.route('/post', methods=["POST"])
def hello_world_():
    tmp = request.json['id']
    if tmp == 1:
        return jsonify({"code": 200, "message": "成功"})
    if tmp == 2:
        return jsonify({"code": 201, "message": "失败"})
    else:
        return jsonify({"code": 203, "message": "异常"})


@app.route('/file', methods=["POST"])
def get_file():
    f = request.files['file']
    f.save("test.png")
    return jsonify({"code": 200, "message": "成功"})


if __name__ == '__main__':
    app.run(debug=True)
