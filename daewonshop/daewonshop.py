# -*- coding: utf-8 -*-
import random
import requests
from bs4 import BeautifulSoup
import telegram
import datetime
from time import sleep

# telegram bot token - nobilibot
bot = telegram.Bot(token = '{token}')

# chat id for sending message
chat_id = '{chat_id}'

# setting random time for login (3 hours)
randomSec = random.randrange(1, 10801)
t = datetime.datetime.now()
t = t + datetime.timedelta(seconds = randomSec)
t = t.strftime('%Y-%m-%d %H:%M:%S')

# send message of predicting time
bot.sendMessage(chat_id = chat_id, text = '* 로그인 예상일시\n> ' + t)

# sleep during random time
sleep(randomSec)

# declare variables
USER_ID = '{user_id}'
USER_PW = '{user_pw}'
loginUrl = 'https://www.daewonshop.com/member/login_ps.php'
mypageUrl = 'https://www.daewonshop.com/mypage/index.php'

# param for login
param = {
  'mode'      : 'login',
  'returnUrl' : mypageUrl,
  'loginId'   : USER_ID,
  'loginPwd'  : USER_PW,
  'saveId'    : 'y',
}

session = requests.session()

# login
res = session.post(loginUrl, data = param)
res.raise_for_status()

# mypage
res = session.get(mypageUrl)
res.raise_for_status()

# check mileage
soup = BeautifulSoup(res.text, 'html.parser')
mileage = soup.select('.point-item.mileage > div > div > a > span')[0].text

# send message of mileage
bot.sendMessage(chat_id = chat_id, text = '* 로그인 완료\n> 적립금 : ' + mileage + 'P')
