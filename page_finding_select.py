import requests
from bs4 import BeautifulSoup
page_num = int(input("輸入你想要尋找的頁數(頭)"))
page_num_1 = int(input("輸入你想要尋找的頁數(尾)"))
url = 'https://www.ptt.cc/'
for j in reversed(range(page_num_1, page_num)):
    web = requests.get("https://www.ptt.cc/bbs/Beauty/index%d.html" %
                       j, cookies={'over18': '1'})
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')
    #divs = soup.find('div', class_='bbs-screen bbs-content')
    if len(titles) == 0:
        print('404 not found ')
        break
    else:
        for i in titles:
            if i.find('a') != None:
                print(i.find('a').get_text())
                print(url+i.find('a')['href'], end='\n\n')
