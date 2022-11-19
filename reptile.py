import requests
from bs4 import BeautifulSoup


def PTT_Gossiping():
    url = 'https://www.ptt.cc/'
    web_1 = requests.get(
        'https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18': '1'})
    soup = BeautifulSoup(web_1.text, 'html5lib')
    titles = soup.find_all('div', class_='title')

    for i in titles:
        if i.find('a') != None:
            print(i.find('a').get_text())
            print(url+i.find('a')['href'], end='\n\n')


def Gamer():
    url = 'https://forum.gamer.com.tw/'
    web = requests.get('https://forum.gamer.com.tw/B.php?bsn=60076')
