import requests
from bs4 import BeautifulSoup


def board_get(board):
    url = 'https://www.ptt.cc/'
    web = requests.get(
        'https://www.ptt.cc/bbs/%s/index.html' % board, cookies={'over18': '1'})
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')

    for i in titles:
        if i.find('a') != None:
            print(i.find('a').get_text())
            print(url+i.find('a')['href'], end='\n\n')


board_name = str(input("請輸入想要爬的板(英文)："))
board_get(board_name)
