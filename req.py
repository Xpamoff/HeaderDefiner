import json, urllib.request

token = 'AQAAAAATz2ALAAfGKxA_tjoNVk5ivNjTlx1yQ1o'
url = 'https://api-sandbox.direct.yandex.ru/v4/json/'

data0 = {
   'token': token,
   'method': 'GetWordstatReport',
   'param': 6717077
}
jdata2 = json.dumps(data0, ensure_ascii=False).encode('utf8')

response2 = urllib.request.urlopen(url,jdata2)
data = response2.read().decode('utf8')
#print(data)
jdata = json.loads(data)
print(jdata)
print(jdata['data'][0]['SearchedAlso'][0])

#for i in jdata['data']['SearchedAlso']:
 #  print(i)

# file_1 = open("file.json", "w")
#
# file_1.write(str(jdata))
#
# file_1.close()