import urllib
import requests
import json


def run(uid, price,d1,d2,d3,d4):
    url = "http://localhost/book.php"
    response = requests.post(url, data={'uid': uid, 'price': price, 'd1': int(d1), 'd2': int(d2), 'd3': int(d3), 'd4': int(d4)})
    print(response.text)
    if int(response.text) == 0:
        print("不够钱")
        return 0
    else:
        print("ok")
        return 1

#run("s2", 1)

