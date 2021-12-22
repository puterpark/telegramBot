# spamhaus

### 스팸하우스 IP 등재 확인 알림봇

#### 요약

1. spamhaus.sh를 크론탭으로 실행
```
*/15 * * * * spamhaus.sh 92.x.x.77
```
2. 매 실행마다 설정한 IP를 스팸하우스에 DNS LookUp을 하고, 해당 IP가 등재되었을 경우 spamhaus.py를 실행시켜 텔레그램으로 알림 전달

---

#### 소스 역할

`spamhaus.sh`
> 인자로 받은 IP를 스팸하우스에 DNS LookUp을 하고, 해당 IP가 등재되었다는 응답을 받으면 spamhaus.py를 구동하는 역할

`spamhaus.py`
> 텔레그램으로 알림을 전달하는 역할