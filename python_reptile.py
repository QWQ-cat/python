import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies = {'over18':'1'})
soup = BeautifulSoup(web.text , 'html5lib')
soup.remove
print(soup.title)