import requests
from bs4 import BeautifulSoup
from random import choice
def get_sslproxy():
    r = requests.get('https://www.sslproxies.org')
    soup = BeautifulSoup(r.text, 'lxml')
    tab = soup.find('tbody')
    proxies = []
    for i in range(20):
        ip_proxy = tab.contents[i].contents[0].text.strip()
        port = tab.contents[i].contents[1].text.strip()
        proxy_string = ip_proxy + ':' + port
        proxies.append(proxy_string)
    return proxies

def get_html(url):
    with open('useragents.txt') as f:
        useragents = f.read().split('\n')
    proxies = get_sslproxy()
    proxy = {'http': 'http://'+choice(proxies)}
    useragent = {'User-Agent': choice(useragents)}
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text

def get_ip(html):
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)


def main():
    for i in range(10):
        try:
            get_ip(get_html('http://sitespy.ru/my-ip'))
        except:
            continue

if __name__ == '__main__':
    main()
