import requests
from bs4 import BeautifulSoup

hotpage = requests.get('https://www.ptt.cc/bbs/hotboards.html')
soup = BeautifulSoup(hotpage.text, 'html5lib')
# print(soup)
board_find = soup.find_all('a', class_='board')
for board in board_find:
    header_name = board.find('div', class_='board-name')
    print("看板名稱：", header_name.text)
    header_page = board.select('span')[0]
    print("看板分類文章數：", header_page.text)
    header_classes = board.find('div', class_='board-class')
    print("看板分類：", header_classes.text)
    header_title = board.select('div.board-title')[0]
    print("看板標題：", header_title.text)
    header_url = 'https://www.ptt.cc' + board['href']
    print("看板網址：" + header_url)
    print('\n\n')
