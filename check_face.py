import base64
import urllib
import requests
import json


API_KEY = "usB297au143OeqjZ8sxulz3l"
SECRET_KEY = "Fwreu4mHHdQY9qdA3XwTgHr5s3dPkUgp"
def run(path):
    url = "https://aip.baidubce.com/rest/2.0/face/v3/search?access_token=" + get_access_token()

    a = get_file_content_as_base64(path)
    payload = json.dumps({
        "group_id_list": "1",
        "image": a,
        "image_type": "BASE64"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)
    res = json.loads(response.text)
    if res['error_code']==0:
        uid = res['result']['user_list'][0]['user_id']
        score = res['result']['user_list'][0]['score']
        #print(score)
        if score >= 75:
            print(uid)
            return uid
        else:
            print(0)
            return "s0"
    # os.remove(path) #删除临时照片

def get_file_content_as_base64(path, urlencoded=False):
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

#path = "th.jpg"
#run(path)