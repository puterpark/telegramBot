# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import telegram

# telegram bot token
bot = telegram.Bot(token = '{token}')

# chat id for sending message
chat_id = '{chat_id}'

# current dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# declare variables
rootUrl = 'https://maplestory.nexon.com'

dic = {
  'newsUrl'   : 'https://maplestory.nexon.com/News/Notice',
  'updateUrl' : 'https://maplestory.nexon.com/News/Update',
  'eventUrl'  : 'https://maplestory.nexon.com/News/Event',
  'cashUrl'   : 'https://maplestory.nexon.com/News/CashShop',
  'news'      : '공지사항',
  'update'    : '업데이트',
  'event'     : '이벤트',
  'cash'      : '캐시샵 공지'
}

urlList = ['news', 'update', 'event', 'cash']

# def getValue by dic
def getValue(key):
  return dic[key]

# loop for urlList
for l in urlList:
  # target link for list
  url = getValue(l + 'Url')
  req = requests.get(url)
  req.encoding = 'utf-8'

  html = req.text

  targetPath = ''

  # get target url
  targetPath = BeautifulSoup(html, 'html.parser').find('div', {'class' : l + '_board'}).findAll('a')[0]['href']
  targetUrl = rootUrl + targetPath

  # get target post number
  targetPostNo = targetUrl.split('/')[-1]

  # target url for targetPostTitle
  req = requests.get(targetUrl)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  targetTitle = soup.find('p', {'class' : 'qs_title'}).text.strip()
  targetTitle = '[' + getValue(l) + '] ' + targetTitle

  # newsPostNo, updatePostNo, eventPostNo, cashPostNo
  fileName = 'postNo/' + l + 'PostNo.txt'

  # read '{notice/update/event/cashshop}PostNo.txt'
  with open(os.path.join(BASE_DIR, fileName), 'r') as f_read:
    before = f_read.readline()
    f_read.close()

    # compare beforeNo with targetPostNo
    if before < targetPostNo:
      # change target url for mobile
      targetUrl = targetUrl.replace('maplestory.', 'm.maplestory.')
      #send message title & url
      bot.sendMessage(chat_id = chat_id, text = targetTitle + '\n' + targetUrl)
      with open(os.path.join(BASE_DIR, fileName), 'w+') as f_write:
        f_write.write(targetPostNo)
        f_write.close()
