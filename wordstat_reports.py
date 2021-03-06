import json, urllib.request
import time
import get_token

url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
token = get_token.token


def create_report(token, phrase):
    data = {
        'method': 'CreateNewWordstatReport',
        'token': token,
        'locale': 'ru',
        'param': {
            "Phrases": phrase,
            "GeoID": [
                0
            ]
        }
    }

    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
    response = urllib.request.urlopen(url, jdata)
    num = response.read().decode('utf8')

    id = ''
    for i in range(8, len(num) - 1):
        id = id + (str(num[i]))
    print('Запрос сформирован')
    return id


def get_report(token, report_id):
    data = {
        'token': token,
        'method': 'GetWordstatReport',
        'param': report_id
    }
    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
    response = urllib.request.urlopen(url, jdata)
    report_str = response.read().decode('utf8')
    report_dict = json.loads(report_str)
    try:
        report = report_dict['data'][0]['SearchedAlso']
        return report
    except KeyError:
        print(report_dict)
        return -1


def phrase_choose(report):
    a = []
    sorted_report = sorted(report, key=lambda d: d['Shows'], reverse=True)
    count = 0
    for i in sorted_report:
        a.append(i['Phrase'] + ": " + str(i['Shows']))
        count += 1
        if count == 5:
            break
    return a


if __name__ == "__main__":
    report_id = create_report(token, ["сброс веса"])
    time.sleep(10)
    new_report = get_report(token, report_id)
    if new_report != -1:
        phrase_choose(new_report)
