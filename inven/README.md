# inven

### 인벤 경험치 알림봇

#### 요약

1. inven.py를 크론탭으로 실행
```
0 13 * * * /usr/bin/python3 inven.py
```
2. 3시간 범위에서 랜덤한 시간이 지난 뒤 로그인하도록 구현
3. ID/PW를 이용하여 로그인 한 뒤 경험치 현황을 텔레그램으로 알림 전달