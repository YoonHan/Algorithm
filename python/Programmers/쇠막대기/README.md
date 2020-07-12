# 쇠막대기

## 핵심 포인트

> https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3#

- 스택을 이용하면 쉽게 풀 수 있는 문제이다.
- 처음에는 쇠막대기 각각을 따로 파악해서 각 쇠막대기에 몇개의 레이저가 지나가는지 파악하는 식으로 푸려고 했으나 1번의 문자열 탐색으로(즉, `O(n)` 으로) 풀 수 있는 방법이 없는지 고민했다.
- 스택을 사용하여 조금만 고민하면 쉽게 풀 수 있다. 풀이는 다음과 같다.

```python
def solution(arrangement):
    스택 선언

    for 현재 문자 in arrangement:
        if 현재 문자 == '(': 스택에 넣음
        elif 이전에 탐색한 문자 == '(' and 현재 문자 == ')':
            스택에서 pop 
            정답 변수 += 스택의 길이
        elif 이전에 탐색한 문자 == ')' and 현재 문자 == ')':
            스택에서 pop
            정답 변수 += 1
        이전에 탐색한 문자 = 현재 문자
    
    return 정답 변수
```