import requests
from bs4 import BeautifulSoup

page_num = int(input("輸入你想要尋找的頁數"))
url = 'https://www.ptt.cc/'
web = requests.get("https://www.ptt.cc/bbs/Beauty/index%d.html" %
                   page_num, cookies={'over18': '1'})
soup = BeautifulSoup(web.text, 'html5lib')
titles = soup.find_all('div', class_='title')
#content = soup.find_all('div', class_="bbs-screen.bbs-content")
if len(titles)==0:
    print("404 Not Found.")
else:
    for i in titles:
        if i.find('a') != None:
            print(i.find('a').get_text())
            print(url+i.find('a')['href'], end='\n\n')
