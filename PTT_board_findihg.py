import requests
from bs4 import BeautifulSoup


url = 'https://www.ptt.cc/bbs/'
web = requests.get('https://www.ptt.cc/bbs/index.html')
soup = BeautifulSoup(web.text, 'html5lib')
board_name = soup.find_all('div', class_='board-name')
hot = soup.find_all('span', class_='hl f6')
board_class = soup.find_all('div', class_='board-class')
board_title = soup.find_all('div', class_='board-title')
'''
print(board_name, end=' ')
print(board_class, end='*')
print(board_title, end='~')
'''
# https://ithelp.ithome.com.tw/articles/10228998?sc=pt
for i in board_name:
    if i.find('board-name') != None:
        print(board_name[i], ' ', hot[i], ' ',
              board_class[i], ' ', board_title[i], '\n')
        print(url+board_name[i])
