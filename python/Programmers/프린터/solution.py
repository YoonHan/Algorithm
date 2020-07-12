from collections import deque


def solution(priorities, location):
    answer = 0
    pairs = [[priority, False] for priority in priorities]
    pairs[location][1] = True
    pairs = deque(pairs)
    start = 1
    while pairs:
        current = pairs.popleft()
        is_top_prior = True
        for p, is_selected in pairs:
            if p > current[0]:
                pairs.append(current)
                is_top_prior = False
                break
        if is_top_prior:
            if current[1] == True:
                answer = start
                break
            elif current[1] == False:
                start += 1

    return answer
