import requests
import progressbar
from bs4 import BeautifulSoup as bs


def pars(name, surname, url):  # функция парсера
    url = f"https://www.teoma.com/web?q='{name} {surname} | {surname} {name} site:{url}'"
    headers = {'accept': '*/*'}
    session = requests.Session()
    request = session.get(url)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('li', {"class": 'algo-result'})
        var = len(divs)
        if var > 0:
            print(f"По запросу {name} {surname} найдено {var} вхождение на сайте {url} Узнать подробности?")
    else:
        print('Error!')


def test_func(name, surname):
    with open('vuz.txt', 'r') as vuz_list:
        for url in progressbar.progressbar(vuz_list.readlines(), suffix='{seconds_elapsed:.1}'):
            pars(name, surname, url)


if __name__ == '__main__':
    name = input(str('Введите фамилию искомого человека: '))
    surname = input(str('Введите имя: '))
    test_func(name, surname)