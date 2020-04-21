from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline


def get_max(m):
    mv = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] > mv:
                mv = m[i][j]
    return mv


def change_max_val(m):
    global max_value  # 전역 변수
    for i in range(N):
        for j in range(N):
            if m[i][j] > max_value:
                max_value = m[i][j]


def move(m, d):
    new = deepcopy(m)
    if d == 0:  # 동
        merged = []
        for r in range(0, N):
            for c in range(N - 1, -1, -1):
                y = c
                if new[r][y] == 0:
                    continue
                while y + 1 < N:
                    if new[r][y + 1] == 0:
                        new[r][y + 1] = new[r][y]
                        new[r][y] = 0
                    elif new[r][y] == new[r][y + 1] and (r, y + 1) not in merged:
                        new[r][y + 1] *= 2
                        new[r][y] = 0
                        merged.append((r, y + 1))
                        break
                    else:
                        break
                    y += 1
    elif d == 1:  # 서
        merged = []
        for r in range(0, N):
            for c in range(0, N):
                y = c
                if new[r][y] == 0:
                    continue
                while y - 1 >= 0:
                    if new[r][y - 1] == 0:
                        new[r][y - 1] = new[r][y]
                        new[r][y] = 0
                    elif new[r][y] == new[r][y - 1] and ((r, y - 1) not in merged):
                        new[r][y - 1] *= 2
                        new[r][y] = 0
                        merged.append((r, y - 1))
                        break
                    else:
                        break
                    y -= 1
    elif d == 2:  # 남
        merged = []
        for c in range(0, N):
            for r in range(N - 1, -1, -1):
                y = r
                if new[y][c] == 0:
                    continue
                while y + 1 < N:
                    if new[y + 1][c] == 0:
                        new[y + 1][c] = new[y][c]
                        new[y][c] = 0
                    elif new[y][c] == new[y + 1][c] and (y + 1, c) not in merged:
                        new[y + 1][c] *= 2
                        new[y][c] = 0
                        merged.append((y + 1, c))
                        break
                    else:
                        break
                    y += 1
    elif d == 3:  # 북
        merged = []
        for c in range(0, N):
            for r in range(0, N):
                y = r
                if new[y][c] == 0:
                    continue
                while y - 1 >= 0:
                    if new[y - 1][c] == 0:
                        new[y - 1][c] = new[y][c]
                        new[y][c] = 0
                    elif new[y - 1][c] == new[y][c] and (y - 1, c) not in merged:
                        new[y - 1][c] *= 2
                        new[y][c] = 0
                        merged.append((y - 1, c))
                        break
                    else:
                        break
                    y -= 1
    return new


def solution(m, depth):
    if depth > 5:
        return
    change_max_val(m)   # 보드판 전체 요소랑, 전역 변수 max_value 랑 값 비교 후 최대값 갱신
    for d in ways:        # ways 는 0(동), 1(서), 2(남), 3(북) 저장된 배열
        new_m = move(m, d)  # 보드판 m 을 가지고 d 방향으로 움직였을 때 결과 보드판을 new_m 에 저장
        solution(new_m, depth + 1)  # 다음 depth 로 새로운 보드판 전달
    return


N = int(input())
m = [list(map(int, (input().split()))) for _ in range(N)]
ways = [0, 1, 2, 3]
max_value = -1
solution(m, 0)
print(max_value)
