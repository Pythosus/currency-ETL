import requests
from bs4 import BeautifulSoup
import re


#парсер валют
def currency_parser(url) -> list:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    data = []
    #запрос
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    sp = soup.find_all('tr')
    #обработка
    for x in sp:
        dt = x.find_all('td')
        for i in range(len(dt)):
            dt[i] = str(dt[i]).strip('<td>').strip('</td>')
            if dt[i][0].isdigit():
                if ',' in dt[i]:
                    dt[i] = float(dt[i].replace(',', '.'))
                else:
                    dt[i] = int(dt[i])
        data.append(dt)
    return data[1:]


#парсер криптовалют
def crypto_parser(url) -> list:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    #запрос
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    sp_name = soup.find_all('div',
                             class_='tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5')
    sp_cost = soup.find_all('td', class_='tw-text-end')
    # обработка
    data_cost = [x.get_text() for x in sp_cost]
    data_cost = [float(re.sub(r'[^\d,.]', '', data_cost[i]).replace(',', '.'))
                 for i in range(len(data_cost)) if i % 10 == 0]
    data_name = [[y.strip(' ') for y in x.get_text().split('\n') if y.strip(' ') != ''] for x in sp_name][1:-8]
    #print(max([len(x[-1]) for x in data_name]), max([len(x[0]) for x in data_name])) <- определение параметров для БД
    data = [[data_name[i][1], data_name[i][0], data_cost[i]] for i in range(len(data_cost))]

    return data

print(crypto_parser('https://www.coingecko.com/ru'))
#print(currency_parser('https://cbr.ru/currency_base/daily'))
