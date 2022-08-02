import requests
from bs4 import BeautifulSoup


URL = 'https://www.accuweather.com/ru/kg/bishkek/222844/weather-forecast/222844'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# html = get_html(URL)


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='card weather-card content-module non-ad')
    weather = []
    for item in items:
        weather.append({
            'date': item.find('span', class_='sub-title').getText(),
            'date_descr': item.find('h2').getText(),
            # 'time': item.find("p", class_='sub').getText(),
            'temp': item.find("div", class_='temp').getText()[0:3],
            'real_feel': item.find("div", class_='real-feel').getText()[10:],
            'descr': item.find("div", class_='phrase').getText(),
            # 'link': 'https://www.accuweather.com/ru/kg/bishkek/222844/weather-forecast/222844',
            # 'photo': 'https://www.accuweather.com'+item.find_next('svg', class_='icon-weather').get('data-src')
        })
    return weather


# print(get_data(html.text))


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = get_data(html.text)
        return answer
    else:
        raise Exception('Error in parser')


# URL_currencies = 'https://www.nbkr.kg/'
#
# HEADERS_currencies = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#     }


# def get_html_currencies(url, params=''):
#     req = requests.get(url, headers=HEADERS, params=params)
#     return req
#
#
# html_2 = get_html(URL_currencies)


# def get_data_currencies(html):
#     soup = BeautifulSoup(html, "html.parser")
#     items = soup.find_all('div', class_='sticker-body')
#     currencies = []
#     for item in items:
#         currencies.append({
#             'USD': item.find('td', class_='exrate')
#         })
#     return currencies[2]['USD'][0:]
#
#
# print(get_data_currencies(html_2.text))

