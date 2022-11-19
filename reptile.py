import requests
from bs4 import BeautifulSoup


def PTT_Gossiping(n):
    url = 'https://www.ptt.cc/'
    web = requests.get(
        'https://www.ptt.cc/bbs/Gossiping/index%d.html' % n, cookies={'over18': '1'})
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')

    for i in titles:
        if i.find('a') != None:
            print(i.find('a').get_text())
            print(url+i.find('a')['href'], end='\n\n')


def WorldCup(n):
    url = 'https://www.ptt.cc/'
    web = requests.get('https://www.ptt.cc/bbs/WorldCup/index%d.html' % n)
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')
    for j in titles:
        if j.find('a') != None:
            print(j.find('a').get_text())
            print(url+j.find('a')['href'], end='\n\n')


def Beauty(n):
    url = 'https://www.ptt.cc/'
    web = requests.get(
        'https://www.ptt.cc/bbs/Beauty/index%d.html' % n, cookies={'over18': '1'})
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')
    for k in titles:
        if k.find('a') != None:
            print(k.find('a').get_text())
            print(url+k.find('a')['href'], end='\n\n')


text = input("想爬蟲的板:")
page_num = int(input("想爬的頁面:"))
if text == '八卦版':
    PTT_Gossiping(page_num)
elif text == '世界盃':
    WorldCup(page_num)
elif text == '表特版':
    Beauty(page_num)
