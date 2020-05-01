from itertools import combinations
import math

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]


def make_sections():
    global N
    global A
    # 구하려는 경계가 지도를 벗어나는지 체크
    # d1 = 좌하, d2 = 우하
    border_infos = []
    candidates = []
    for r in range(N):
        for c in range(N):
            for d1 in range(1, N - 1):
                for d2 in range(1, N - d1):
                    if r + d1 + d2 >= N or c - d1 < 0 or c + d2 >= N:
                        continue
                    border_infos.append((r, c, d1, d2))
    # 구획 나누고 인구 수 차이 체크
    for r, c, d1, d2 in border_infos:
        count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        top = (r, c)
        left = (r + d1, c - d1)
        right = (r + d2, c + d2)
        bottom = (r + d1 + d2, c - d1 + d2)
        # A의 인구 수를 알맞은 구역에 각각 누적
        start, end = c, c
        for _r in range(N):
            if _r > top[0] and left[0] - _r >= 0:
                start -= 1
            elif _r > top[0] and left[0] - _r < 0:
                start += 1

            if _r > top[0] and right[0] - _r >= 0:
                end += 1
            elif _r > top[0] and right[0] - _r < 0:
                end -= 1

            for _c in range(N):
                if top[0] <= _r <= bottom[0] and start <= _c <= end:
                    count[5] += A[_r][_c]
                else:
                    if _r < left[0] and _c <= top[1]:
                        count[1] += A[_r][_c]
                    elif _r <= right[0] and top[1] < _c:
                        count[2] += A[_r][_c]
                    elif _r >= left[0] and bottom[1] > _c:
                        count[3] += A[_r][_c]
                    elif _r > right[0] and bottom[1] <= _c:
                        count[4] += A[_r][_c]
        # 인구 수 차이 최솟값 구하기
        values = count.values()
        max_popu = max(values)
        min_popu = min(values)
        candidates.append(max_popu - min_popu)

    return min(candidates)


def solution():
    global N, A
    print(make_sections())


solution()
