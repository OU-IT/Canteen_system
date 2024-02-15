import urllib
import requests
import json


def run(uid):
    url = "http://localhost/get_rest_moeny.php"
    response = requests.post(url, data={'uid': uid})
    print(response.text)
    return float(response.text)
#run("s27")

