# coding: utf8
import requests
import progressbar
from bs4 import BeautifulSoup as bs


def strnum(file):
    numstr = sum(1 for line in open(file, 'r'))
    return numstr


def pars(name, surname, url):  # функция парсера

    url = 'https://www.teoma.com/web?q="' + name + ' ' + surname + '" | "' + surname + ' ' + name + '" site:' + url
    headers = {'accept': '*/*'}
    session = requests.Session()
    request = session.get(url)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('li', {"class": 'algo-result'})
        var = len(divs)
        if var > 0:
            var = str(var)
            print(
                ' По запросу ' + name + " " + surname + " найдено " + var + " вхождение на сайте " + url + " Узнать подробности?")
    else:
        print('Error!')


numstr = strnum('vuz.txt')
name = input(str('Введите фамилию искомого человека: '))
surname = input(str('Введите имя: '))
# name = input(str('Введите Фамилию искомого человека: '))
# surname = input(str('Имя: '))'''

bar = progressbar.ProgressBar(maxval=numstr).start()
line = 0
while line < numstr:
    bar.update(line)
    f = open('vuz.txt')
    lines = f.readlines()
    url = lines[line]
    pars(name, surname, url)
    line += 1
bar.finish()