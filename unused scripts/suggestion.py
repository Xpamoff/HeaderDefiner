import json, urllib.request
import time
import get_token

url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
token = get_token.token


def create_report(token, phrase):
    data = {
        'method': 'GetKeywordsSuggestion',
        'token': token,
        'locale': 'ru',
        'param': {
            "Keywords": phrase
        }
    }

    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
    response = urllib.request.urlopen(url, jdata)
    num = response.read().decode('utf8')

    return str(num)


# def get_report(token, report_id):
#     data = {
#         'token': token,
#         'method': 'GetWordstatReport',
#         'param': report_id
#     }
#     jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
#     response = urllib.request.urlopen(url, jdata)
#     report_str = response.read().decode('utf8')
#     report_dict = json.loads(report_str)
#     try:
#         report = report_dict
#         return report
#     except KeyError:
#         print(report_dict)
#         return -1


if __name__ == "__main__":
    report_id = create_report(token, ["купить", "айфон"])
    # time.sleep(25)
    # new_report = get_report(token, report_id)
    print(report_id)

