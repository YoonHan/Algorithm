from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    waiting = deque(truck_weights)
    passing = deque([0] * bridge_length)
    weight_on_bridge = 0
    while len(waiting) != 0:
        answer += 1
        weight_on_bridge -= passing.popleft()
        if weight_on_bridge + waiting[0] <= weight:
            truck = waiting.popleft()
            passing.append(truck)
            weight_on_bridge += truck
        else:
            passing.append(0)

    answer += bridge_length
    return answer
