# -*- coding: utf-8 -*-
import random
import telegram
import datetime
from playwright.sync_api import Playwright, sync_playwright
from time import sleep

# 텔레그램 봇 토큰 - nobilibot
bot = telegram.Bot(token = '{token}')

# 메시지를 전달할 chat_id
chat_id = '{chat_id}'

# 로그인을 위한 랜덤 시간 설정 (1초 ~ 3시간)
randomSec = random.randrange(1, 10801)
t = datetime.datetime.now()
t = t + datetime.timedelta(seconds=randomSec)
t = t.strftime('%Y-%m-%d %H:%M:%S')

# 로그인 예상 일시 메시지 전달
bot.sendMessage(chat_id = chat_id, text = '* 인벤 로그인 예상일시\n> ' + t)

# 랜덤 시간동안 sleep
sleep(randomSec)

USER_ID = '{USER_ID}'
USER_PW = '{USER_PW}'

def run(playwright: Playwright) -> None:

  # 크롬 브라우저 실행
  browser = playwright.chromium.launch()
  context = browser.new_context()

  # 새로운 웹페이지 오픈
  page = context.new_page()

  # 인벤 로그인 페이지로 이동
  page.goto('https://member.inven.co.kr/user/scorpio/mlogin')

  # 아이디 요소 클릭
  page.click('#user_id');

  # 아이디 요소에 아이디 채우기
  page.fill('#user_id', USER_ID);

  # 아이디 요소에서 Tab 누르기
  page.press('#user_id', 'Tab');

  # 비밀번호 요소에 비밀번호 채우기
  page.fill('#password', USER_PW);

  # 패스워드 요소에서 Enter 누르기
  with page.expect_navigation():
    page.press('#password', 'Enter');

  # 인벤 정보 페이지로 이동
  page.goto('https://www.inven.co.kr/member/inventory')

  # 경험치 관련 내용 크롤링
  # ['', '120,435', '(41%)', '/135,001', '(다음레벨까지14,566/마격까지13,315남음', ')', '', '']
  HTML = page.inner_text('body > div.inventory-setting > div.inventory-content-wrap.inventory-skin > div > div.inventory-section.pcskin > div.inventory_content_wrap > div.inventory_content.memberProfileS2 > div.iv_cont.clear > div.info_wrap > dl > dd.exp').replace(' ', '').split('\n')

  # 120,435/135,001 (41%)
  HTML = HTML[1] + HTML[3] + ' ' + HTML[2]

  bot.sendMessage(chat_id = chat_id, text = '* 인벤 로그인 완료\n> ' + HTML)

  context.close()
  browser.close()

with sync_playwright() as playwright:
  run(playwright)
