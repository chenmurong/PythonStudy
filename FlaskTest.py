# 导入类库
from flask import Flask, request, jsonify
import requests

# 创建实例
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def login():
    req_data = request.get_json()
    print( req_data)
    msg_type = req_data.get("msg_type", "null")
    res = {"name":"cmr"}
    logic()
    # return jsonify({'user': "cmr"}),200
    # return "receive msg {0}".format(msg_type)
    # return '%s jjjj %s' % (password , user_name)
def logic():
    return jsonify({'user': "cmr"}), 200

def notify_client():
    url = "http://localhost:5005/"
    requests.post(url, json= {
        "msg_type": "RequestHello"
    })
    print("send success")
    pass

# 启动实例
if __name__ == '__main__':
    app.run(debug=True)
