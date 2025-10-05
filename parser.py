import requests
from bs4 import BeautifulSoup


def currency_parser(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    data = []
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    sp = soup.find_all('tr')

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


def crypto_parser(url):
    pass