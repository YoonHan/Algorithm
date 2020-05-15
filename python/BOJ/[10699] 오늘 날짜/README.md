# 오늘 날짜

## 핵심 포인트 

- 파이썬으로 날짜 자료형을 다루는 기초적인 문제.
- 기초적이지만 중요한 내용을 담고 있음
- aware datetime / naive datetime 두 형식이 상호 호환이 불가능한 형식임을 알게 되었다. 참고로 aware datetime은 timezone을 포함하고 있는 것이고 naive는 해당 정보가 빠져있는 것이다.
- datetime.timezone()으로 timezone을 설정해주고, datetime.datetime.now()에 인자로 넘겨주어 설정한 timezone에 대한 지금 시간값을 얻어낸다.