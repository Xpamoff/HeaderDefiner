import json, urllib.request
import time

url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
token = 'AQAAAAATz2ALAAfGKxA_tjoNVk5ivNjTlx1yQ1o'


def create_report(token, phrase):
    data = {
        'method': 'CreateNewWordstatReport',
        'token': token,
        'locale': 'ru',
        'param': {
            "Phrases": [
                phrase
            ],
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
    sorted_report = sorted(report, key=lambda d: d['Shows'], reverse=True)
    print(sorted_report)
    count = 0
    for i in sorted_report:
        print(i['Phrase'] + ": " + str(i['Shows']))
        count += 1
        if count == 5:
            break


report_id = create_report(token, "путин умер")
time.sleep(6)
new_report = get_report(token, report_id)
if new_report != -1:
    phrase_choose(new_report)
