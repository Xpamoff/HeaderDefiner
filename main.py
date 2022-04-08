import json, urllib.request

url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
token = 'AQAAAAATz2ALAAfGKxA_tjoNVk5ivNjTlx1yQ1o'

data = {
   'method': 'CreateNewWordstatReport',
   'token': token,
   'locale': 'ru',
   'param': {
      "Phrases": [
         "Макароны с кетчупом"
      ],
      "GeoID": [
         0
      ]
   }
}
#конвертировать словарь в JSON-формат и перекодировать в UTF-8
jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
response = urllib.request.urlopen(url, jdata)
num = response.read().decode('utf8')

a = ""
for i in range(8, len(num)-1):
    a = a + (str(num[i]))
print(int(a))


