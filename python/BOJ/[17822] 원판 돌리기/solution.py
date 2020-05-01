from collections import deque, defaultdict

N, M, T = list(map(int, input().split()))
circles = {(i + 1): deque([*map(int, input().split())]) for i in range(N)}
commands = [[*map(int, input().split())] for _ in range(T)]


def solution():
    global N, M, T
    global circles
    answer = 0

    for x, d, k in commands:
        # 원판 돌리기
        for key, circle in circles.items():
            if key % x == 0:
                circles[key].rotate(((-1)**d)*k)    # 0 시계 1 반시계
        # 한 원판에 인접한 같은 수들 저장
        removed = defaultdict(list)
        for key, circle in circles.items():
            for idx in range(len(circle)):
                if idx == len(circle) - 1:  # 같은 원판의 끝 원소와 첫 원소 비교 상황 예외 처리
                    if circle[idx] == circle[0] and circle[idx] != 'x':
                        if idx not in removed[key]:
                            removed[key].append(idx)
                        if 0 not in removed[key]:
                            removed[key].append(0)
                else:
                    if circle[idx] == circle[idx + 1] and circle[idx] != 'x':
                        if idx not in removed[key]:
                            removed[key].append(idx)
                        if (idx + 1) not in removed[key]:
                            removed[key].append(idx + 1)
        # 다른 원판과 인전합 같은 수들 저장
        for order in range(0, M):
            for which in range(1, N):
                if circles[which][order] == circles[which + 1][order] and circles[which][order] != 'x':
                    if order not in removed[which]:
                        removed[which].append(order)
                    if order not in removed[which + 1]:
                        removed[which + 1].append(order)
        # 인접한 수들 제거
        if removed.items():
            for key, values in removed.items():
                for idx in values:
                    circles[key][idx] = 'x'
        else:
            count = 0
            sums = 0
            # 평균 구하기
            for key, circle in circles.items():
                for item in circle:
                    if item != 'x':
                        sums += item
                        count += 1
            avg = sums / count
            # 평균보다 큰 수는 1 빼고 작은 수는 1 더하기
            for key, circle in circles.items():
                for idx, item in enumerate(circle):
                    if item != 'x' and item > avg:
                        circle[idx] = item - 1
                    elif item != 'x' and item < avg:
                        circle[idx] = item + 1
        # 모두 지워진 경우 이후 회전 중지
        number_count = 0
        for circle in circles.values():
            for item in circle:
                if item != 'x':
                    number_count += 1
        if number_count == 0:
            break
    # 원판에 적힌 수들의 합 구하기
    for circle in circles.values():
        for item in circle:
            if item != 'x':
                answer += item

    print(answer)


solution()
