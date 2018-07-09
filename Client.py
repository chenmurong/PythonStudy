from flask import Flask, request
import requests

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def handle_msg():
    req_data = request.get_json()
    print( req_data)
    msg_type = req_data.get("msg_type", "null")
    return "receive msg {0}".format(msg_type)

if __name__ == "__main__":
    url = "http://localhost:5000/"
    res = requests.post(url, json= {
        "msg_type": "RequestHello"
    })
    # print( res.text())
    # print(res.url)
    res_dict = res.json()
    username = res_dict.get("user", "default_name")
    print(username)
    print(res_dict['user'])
    print(res.json())