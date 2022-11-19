import requests
from bs4 import BeautifulSoup

page_num = int(input("輸入你想要尋找的頁數"))
url = 'https://www.ptt.cc/'
web = requests.get("https://www.ptt.cc/bbs/Beauty/index%d.html" %
                   page_num, cookies={'over18': '1'})
soup = BeautifulSoup(web.text, 'html5lib')
titles = soup.find_all('div', class_='title')
content = soup.find_all('div', class_1='bbs-screen.bbs-content')
if content == '404 - Not Found.':
    print("找無此頁面")
else:
    for i in titles:
        if i.find('a') != None:
            print(i.find('a').get_text())
            print(url+i.find('a')['href'], end='\n\n')
