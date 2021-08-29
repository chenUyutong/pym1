# coding = utf-8
# 必须添加的模块和包。
import requests
import json
import pyttsx3


id = "595d284bcb7b4d80afffb1f13765773b"# 这里填写自己的密钥
url = 'http://www.tuling123.com/openapi/api?key=' + id + '&info='


while True:

    info = input("我：")

    page = requests.get(url + info)

    json_dic = json.loads(page.text)

    qw=json_dic['text']

    print(('机器人: ' + json_dic['text']))

    ini = pyttsx3.init()

    shuo = ini.say(qw)

    ini.runAndWait()