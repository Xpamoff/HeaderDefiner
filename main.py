import json, urllib.request
import time

url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
token = 'AQAAAAATz2ALAAfGKxA_tjoNVk5ivNjTlx1yQ1o'

data = {
    'method': 'CreateNewWordstatReport',
    'token': token,
    'locale': 'ru',
    'param': {
        "Phrases": [
            "Простуда"
        ],
        "GeoID": [
            0
        ]
    }
}
# конвертировать словарь в JSON-формат и перекодировать в UTF-8

try:
    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
    response = urllib.request.urlopen(url, jdata)
    num = response.read().decode('utf8')

    a = ""
    for i in range(8, len(num) - 1):
        a = a + (str(num[i]))
    print(int(a))
finally:
    time.sleep(2)
    data0 = {
       'token': token,
       'method': 'GetWordstatReport',
       'param': int(a)
    }
    try:
        jdata2 = json.dumps(data0, ensure_ascii=False).encode('utf8')

        response2 = urllib.request.urlopen(url, jdata2)
        data = response2.read().decode('utf8')
        # print(data)
        jdata = json.loads(data)
        print(jdata.data[1].SearchedWith)
    finally:
        print("Success")
