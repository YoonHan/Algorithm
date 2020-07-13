import math
from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    while len(progresses) != 0:
        completed = 0
        head = progresses[0]
        required_time = math.ceil((100 - head) / speeds[0])
        count = 0
        for progress, speed in zip(progresses, speeds):
            if progress + (required_time * speed) >= 100:
                completed += 1
                count += 1
            else:
                break

        for _ in range(count):
            progresses.popleft()
            speeds.popleft()

        answer.append(completed)

    return answer
