
# budongsan

### 네이버 부동산 매물 알림봇

#### 요약

1. 알림봇을 구동하기 앞서 네이버 부동산에서 매물을 확인하고 싶은 지역의 URL을 확인 필요
> 해당 URL 호출 시 매물의 목록을 JSON으로 응답해줌

2. budongsan.sh의 {naver_budongsan_url}을 [1.]의 URL로 변경

3. budongsan.sh를 크론탭으로 실행
```
*/15 * * * * budongsan.sh
```
4. shell 구동 시 설정한 URL의 응답 값인 JSON을 data/data.txt에 저장한 뒤 budongsan.py를 구동
5. data/size.txt에 저장된 파일 크기(실제 data/data.txt의 파일 크기임)와 현재 data/data.txt의 파일 크기를 비교하여 값이 다르면 매물 정보를 텔레그램으로 알림 전달

---

#### 소스 역할

`budongsan.sh`
> 매물정보 URL의 결과값인 JSON을 저장한 뒤 budongsan.py를 구동하는 역할

`budongsan.py`
> 비즈니스 로직을 수행 후 텔레그램으로 알림을 전달하는 역할
> DB에 매물번호가 있을 경우 해당 매물번호는 예외하고 알림 전달

`budongsan_chatbot.py`
> ```
> /usr/bin/python3 budongsan_chatbot.py &
> ```
> 텔레그램 채팅창 내 "/rm" 명령어를 통하여 매물 정보를 예외하는 역할
> 입력한 매물번호를 DB에 insert함

---

#### DB 상세

|이름|데이터 유형|길이/설정|
|:---:|---:|---:|
|budongsanUid|BIGINT|20
```
CREATE TABLE `budongsan` (
	`budongsanUid` BIGINT(20) NOT NULL,
	PRIMARY KEY (`budongsanUid`) USING BTREE
)
```