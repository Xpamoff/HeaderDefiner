import json, urllib.request
import time

url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
token = 'AQAAAAATz2ALAAfGKxA_tjoNVk5ivNjTlx1yQ1o'


def create_report(token, phrase1, phrase2):
    data = {
        'method': 'GetKeywordsSuggestion',
        'token': token,
        'locale': 'ru',
        'param': {
            "Keywords": [
                phrase1,
                phrase2
            ]
        }
    }

    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
    response = urllib.request.urlopen(url, jdata)
    result = response.read().decode('utf8')

    print(result)
    return result

time.sleep(5)
create_report(token, "телефон", "компьютер")
