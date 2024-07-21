# 간단한 네트워크 상태 기록용 스크립트

- KT가 며칠전부터 인터넷이 안되는데 기사 불렀는데 문제가 없으면 비용이 청구된다고 해서 테스트용으로 스크립트 생성
- 당연하게도 네트워크를 제대로 물고 실행해야 하고 되도록이면 공유기 등 별도의 장비가 아닌 모뎀 -> 기기 직결 후 테스트를 해야함

관련 패키지는 아래와 같이 설치

```bash
pipenv install 
```

실행은 아래와 같이 실행

```
# for native
python network_status.py

# for pipenv
pipenv run python network_status.py

```
