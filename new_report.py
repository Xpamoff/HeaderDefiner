#!/usr/bin/python
# -*- coding: utf8 -*-
# import os, sys
# импортируем нужные модули
import json, urllib2, time

# указываем адрес для json запросов
url = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'

# указываем токен доступа
token = AQAAAAAKIa_2AAV1MXS8P7KcHE1FvaDUwDTRpvQ
'AQAAAAAuHqeAAAVNfOtI2abVeUP2p7ymfILUuUEAQAXXXXXXXXXXXXXNPWYl_QEsXXXXXXXXXX3THGzf0'


# функция для формирования отчета
def makeRep():
    # список минус-слов
    negative = ' -бесплатно -бу -дешево'
    # создаем json запрос
    data = {
        # указываем метод вордстат, с которым работаем, в данном случае - создаем отчет
        'method': 'CreateNewWordstatReport',
        # указываем токен доступа
        'token': token,
        # задаем входные параметры; у каждого метода они свои
        'param': {
            # Указываем не более 10 фраз через запятую
            'Phrases': ['айфон 7 цены ростов ' + negative, 'купить колбасу']
            # Указываем нужный регион, если не указали - Все регионы
            # 'GeoID': [213]
        }}
    # Трансформируем json-запрос в одну строку и отправляем в Яндекс:)
    jdata = json.dumps(data, ensure_ascii=False)
    response = urllib2.urlopen(url, jdata)
    # Получаем ответ
    response2 = json.loads(response.read().decode('utf-8'))

    # заносим нужную нам часть ответа в переменную
    id = response2['data']
    # делаем так, что функция на выходе давала номер отчета
    return id


# Функция проверки готовности отчета
def checkRep():
    data = {
        # метод проверки готовности отчета
        'method': 'GetWordstatReportList',
        'token': token
    }
    jdata = json.dumps(data, ensure_ascii=False)
    response = urllib2.urlopen(url, jdata)
    responsedata = json.loads(response.read().decode('utf-8', 'ignore'))

    # Печатаем и подаем на выход информацию о готовности/неготовности отчета
    print(responsedata['data'][len(responsedata['data']) - 1]['StatusReport'])
    return responsedata['data'][len(responsedata['data']) - 1]['StatusReport']


# функц
ия
для
чтения
отчета


def readRep(id):
    # Задаем условие: пока функция проверки готовности не даст положительный ответ, будем ждать
    while checkRep() != 'Done':
        print('...')
        time.sleep(2)

    print(id, ' id')

    data = {
        # используем метод для получения отчета
        'method': 'GetWordstatReport',
        'token': token,
        # указываем номер отчета
        'param': id
    }

    jdata = json.dumps(data, ensure_ascii=False)
    response = urllib2.urlopen(url, jdata)
    responsedata = json.loads(response.read().decode('utf8'))

    # создаем цикл для записи полученных фраз в файл, так как в консоли все фразы могут не поместиться
    i = 0
    # создаем(открываем) txt файл там же, где и наш файл с кодом
    f = open('text.txt', 'w')
    for x in responsedata['data']:

        for ph in responsedata['data'][i]['SearchedWith']:
            print
            ph['Phrase']
            b = str(ph['Phrase'].encode('utf8'))

            # записываем в файл каждую фразу, полученную от Яндекса
            f.write(b + '\n')

        i = i + 1
    print('-------------')
    # закрываем файл
    f.close()


# функция для удаления прочитанных отчетов
def delRep(id):
    data = {
        # метод для удаления отчета
        'method': 'DeleteWordstatReport',
        'token': token,
        # указываем номер отчета и удаляем, он нам бльше не нужен
        'param': id
    }

    jdata = json.dumps(data, ensure_ascii=False)

    response = urllib2.urlopen(url, jdata)
    responsedata = json.loads(response.read().decode('utf8'))

    print(responsedata['data'])
    print('-------------')


# эта функция спаршивает у Яндекса сколько баллов у нас осталось и печатает ответ в консоль
def api():
    data = {
        'method': 'GetClientsUnits',
        'token': token,
        'param': ['andrey.mellodesign']
    }

    jdata = json.dumps(data, ensure_ascii=False)

    response = urllib2.urlopen(url, jdata)
    responsedata = json.loads(response.read().decode('utf8'))

    print(responsedata['data'][0]['UnitsRest'])
    print('-------------')


# вверху было только описание функций, а сама программа идет ниже:)
id = makeRep()
print(id)
readRep(id)
delRep(id)
api()
# конец!
