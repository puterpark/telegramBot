# maplebot

메이플스토리 공지 알림봇

1. maplebot_official.py를 크론탭으로 실행
```
* * * * * /usr/bin/python3 maplebot_official.py
```
2. 매 실행마다 최신 글의 postNo을 확인하여 파일로 저장된 postNo와 다르면 텔레그램으로 알림 전달
```
# 디렉토리 구조
maplebot
 ├maplebot_official.py
 └postNo
   ├cashPostNo.txt
   ├eventPostNo.txt
   ├newsPostNo.txt
   └updatePostNo.txt
```