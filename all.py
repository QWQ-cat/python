import requests
from bs4 import BeautifulSoup


def PTT_board_finding():  # 找尋熱門看板
    hotpage = requests.get('https://www.ptt.cc/bbs/hotboards.html')  # 向網站要求資料
    soup = BeautifulSoup(hotpage.text, 'html5lib')  # 用套件解析
    # 找出所有標籤為"a"且class為'board'的元素，應該是一個列表
    board_find = soup.find_all('a', class_='board')
    for board in board_find:  # 用for迴圈印出來
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


def PTT_page_finding_newest(board):
    url = 'https://www.ptt.cc/'
    web = requests.get('https://www.ptt.cc/bbs/%s/index.html' % board,
                       cookies={'over18': '1'})  # 將所要找尋的看板名稱加到網址中，加入cookies去迴避18歲警告
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')
    for i in titles:
        if i.find('a') != None:
            print(i.find('a').get_text())
            print(url+i.find('a')['href'], end='\n\n')


def PTT_page_finding_select(board):
    page_num = int(input("輸入你想要尋找的頁數"))
    url = 'https://www.ptt.cc/'
    web = requests.get("https://www.ptt.cc/bbs/%s/index%d.html" % board %
                       page_num, cookies={'over18': '1'})
    soup = BeautifulSoup(web.text, 'html5lib')
    titles = soup.find_all('div', class_='title')
    if len(titles) == 0:
        print("404 Not Found.")
    else:
        for i in titles:
            if i.find('a') != None:
                print(i.find('a').get_text())
                print(url+i.find('a')['href'], end='\n\n')


def PTT_page_finding_select_formHead(board):
    page_num = int(input("輸入你想要尋找到的頁數"))
    url = 'https://www.ptt.cc/'
    for j in range(1, page_num):
        web = requests.get("https://www.ptt.cc/bbs/%s/index%d.html" %
                           board % j, cookies={'over18': '1'})
        soup = BeautifulSoup(web.text, 'html5lib')
        titles = soup.find_all('div', class_='title')
        if len(titles) == 0:
            print('404 not found ')
            break
        else:
            for i in titles:
                if i.find('a') != None:
                    print(i.find('a').get_text())
                    print(url+i.find('a')['href'], end='\n\n')


def PTT_page_finding_select_specific(board):
    page_num = int(input("輸入你想要尋找的頁數(頭)"))
    page_num_1 = int(input("輸入你想要尋找的頁數(尾)"))
    url = 'https://www.ptt.cc/'
    for j in reversed(range(page_num_1, page_num)):
        web = requests.get("https://www.ptt.cc/bbs/%s/index%d.html" %
                           board % j, cookies={'over18': '1'})
        soup = BeautifulSoup(web.text, 'html5lib')
        titles = soup.find_all('div', class_='title')
        if len(titles) == 0:
            print('404 not found ')
            break
        else:
            for i in titles:
                if i.find('a') != None:
                    print(i.find('a').get_text())
                    print(url+i.find('a')['href'], end='\n\n')


board_word = {'八卦': 'Gossiping',
              '綜合': 'WorldCup',
              '股票': 'Stock',
              '希洽': 'C_Chat',
              'NBA': 'NBA',
              '省錢': 'Lifeismoney',
              '棒球': 'Baseball',
              '政黑': 'HatePolitics',
              '房屋': 'home-sale',
              '運彩': 'SportLottery',
              '汽車': 'car',
              '表特': 'Beauty',
              '電蝦': 'PC_Shopping',
              '電影': 'movie',
              '西斯': 'sex',
              '寶媽': 'BabyMother',
              '台藍': 'basketballTW',
              '科技': 'Tech_Job',
              '軍事': 'Military',
              '韓星': 'KoreaStar',
              '日本旅遊': 'Japan_Travel',
              '女孩聊天': 'WomenTalk',
              '通訊': 'MobileComm',
              'LoL': 'LoL',
              '男女': 'Boy-Girl',
              '歐兔': 'AllTogether',
              'PM': 'PokeMon',
              'ios': 'iOS',
              'AV女優版': 'japanavgirls',
              'PS5': 'PlayStation',
              'steam': 'Steam',
              '台南': 'Tainan',
              '高雄': 'Kaohsiung',
              'NS': 'NSwitch',
              '日劇': 'Japandrama',
              '就可': 'joke',
              '網購': 'e-shopping',
              '卡版': 'creditcard',
              '台中': 'TaichungBun',
              '媽佛': 'marvel',
              'PoE': 'PathofExile',
              '玄幻': 'CFantasy',
              '硬交': 'HardwareSale',
              '邊緣': 'Marginalman',
              '期權': 'Option',
              'WOW': 'WOW',
              '數位貨幣': 'DigiCurrency',
              'cvs': 'CVS',
              '閒談': 'AC_In',
              '韓劇': 'KoreaDrama',
              '海賊王': 'ONE_PIECE',
              '暗黑': 'DIABLO',
              'PMGO': 'PokemonGO',
              '健身': 'MuscleBeach',
              '新竹': 'Hsinchu',
              '機車': 'biker',
              '美保': 'BeautySalon',
              'GS': 'Gamesale',
              '汽車買賣': 'CarShop',
              'Macshop': 'MacShop',
              '足球八卦版': 'FAPL',
              '軟工': 'Soft_Job',
              '跳蚤': 'forsale',
              'Mobile': 'mobilesales',
              '耳機': 'Headphone',
              '職場': 'Salary',
              '錶板': 'watch',
              '中劇': 'China-Drama',
              '神魔': 'ToS',
              '台綜': 'TW_Entertain',
              '韓綜': 'KR_Entertain',
              '經歷': 'StupidClown',
              'EA': 'EAseries',
              'Lakers': 'Lakers',
              '兄弟': 'Elephants',
              'XBOX': 'XBOX',
              '藝文票卷轉售板': 'Drama-Ticket',
              '獵人': 'Hunter',  # 我打到這裡，你從下一行開始 by蔡桐榮
              '婚姻': 'marriage',
              '美容': 'MakeUp',
              '米哈': 'miHoYo',
              '轉珠': 'PuzzleDragon',
              '銀行': 'Bank_Service',
              '資訊': 'E-appliance',
              '#MLB': 'MLB',
              '原創': 'YuanChuang',
              '贈送': 'give',
              '手遊': 'FATE_GO',
              '生活': 'Key_Mou_Pad',
              '棒球': 'BaseballXXXX',
              '遊戲': 'DMM_GAMES',
              '線上': 'Hearthstone',
              '買賣': 'BabyProducts',
              '資訊': 'Brand',
              '美食': 'fastfood',
              '狩獵': 'MH',
              '資訊': 'Audiophile',
              '布袋': 'Palmar_Drama',
              '音樂': 'KoreanPop',
              '公職': 'PublicServan',
              'NBA.': 'NBA_Film',
              '硬體': 'nb-shopping',
              '男女': 'gay',
              '韓國': 'SuperJunior',
              '理財': 'Insurance',
              '美食': 'Food',
              '寵物': 'cat',
              '攝影': 'DC_SALE',
              '求職': 'part-time',
              '賽馬': 'UmaMusume',
              '交通': 'Aviation',
              '理財': ' e-coupon',
              '碧航': 'AzurLane',
              '烹飪': 'cookclub',
              '咖啡': 'Coffee',
              '大氣': 'TY_Research',
              '交通': 'Railway',
              '硬體': 'Storage_Zone',
              '徵求': 'Wanted',
              '數位': 'Digitalhome',
              '車車': 'SuperBike',
              '考試': 'Examination',
              '彰化': 'ChangHua',
              '宜蘭': 'I-Lan',
              '購三': 'hypermall',
              '桃園': 'Taoyuan',
              '理財': 'MobilePay',
              '旅遊': 'points'}
