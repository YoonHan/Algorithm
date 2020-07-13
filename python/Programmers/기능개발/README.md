# 기능개발

## 핵심 포인트

- 큐를 사용하는 문제다.

```python
def solution(progresses, speeds):
    큐 선언(progresses 와 speeds)

    while progresses queue not empty:
        progresses 의 첫 번째 작업을 완료하는데 걸리는 시간 구하기
        for progresses 의 item 순회하면서:
            if 각 progress + (첫 번째 작업 완료에 걸리는 시간 * 각 speed): 
                완료한 작업 += 1
            else: 
                break
        
        progresses 와 speeds 큐 업데이트
        정답 리스트에 완료한 작업 개수 추가

    return 정답 리스트
```