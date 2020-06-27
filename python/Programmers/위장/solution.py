from collections import Counter


def solution(clothes):
    answer = 1
    # {kind: count} 형식의 Counter 생성
    counter = Counter()
    for name, kind in clothes:
        counter[kind] += 1

    # 모든 조합 수 구하기
    for kind, count in counter.items():
        answer *= count + 1
    answer -= 1  # 아무것도 입지 않은 경우 제외

    return answer
