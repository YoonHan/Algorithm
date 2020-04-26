from copy import deepcopy
import math

N, M = [*map(int, input().split())]
office_map = [[*map(int, input().split())] for _ in range(N)]
cameras = []
answer = math.inf
for r in range(N):
    for c in range(M):
        if 1 <= office_map[r][c] <= 5:
            cameras.append((r, c, office_map[r][c]))


def count(map):
    global N, M
    area = 0
    for r in range(N):
        for c in range(M):
            if map[r][c] == 0:
                area += 1
    return area


def check(m, r, c, dirs):
    # 동 남 서 북 => 0 1 2 3
    global N, M
    next_m = deepcopy(m)
    for dir in dirs:
        if dir == 0:
            for col in range(c + 1, M):
                if m[r][col] != '#':
                    if m[r][col] == 0:
                        next_m[r][col] = '#'
                    elif 1 <= m[r][col] <= 5:
                        continue
                    elif m[r][col] == 6:
                        break
        elif dir == 1:
            for row in range(r + 1, N):
                if m[row][c] != '#':
                    if m[row][c] == 0:
                        next_m[row][c] = '#'
                    elif 1 <= m[row][c] <= 5:
                        continue
                    elif m[row][c] == 6:
                        break
        elif dir == 2:
            for col in range(c - 1, -1, -1):
                if m[r][col] != '#':
                    if m[r][col] == 0:
                        next_m[r][col] = '#'
                    elif 1 <= m[r][col] <= 5:
                        continue
                    elif m[r][col] == 6:
                        break
        elif dir == 3:
            for row in range(r - 1, -1, -1):
                if m[row][c] != '#':
                    if m[row][c] == 0:
                        next_m[row][c] = '#'
                    elif 1 <= m[row][c] <= 5:
                        continue
                    elif m[row][c] == 6:
                        break
    return next_m


def solution(office_map, cameras, idx):
    global answer
    # DFS 종료 조건
    if len(cameras) == idx:
        answer = min(answer, count(office_map))
        return

    r, c, t = cameras[idx]
    # 카메라 타입별로 체크
    if t == 1:
        for i in range(4):
            next_map = check(office_map, r, c, [i])
            solution(next_map, cameras, idx + 1)
    elif t == 2:
        for i in [[0, 2], [1, 3]]:
            next_map = check(office_map, r, c, i)
            solution(next_map, cameras, idx + 1)
    elif t == 3:
        for i in [[3, 0], [0, 1], [1, 2], [2, 3]]:
            next_map = check(office_map, r, c, i)
            solution(next_map, cameras, idx + 1)
    elif t == 4:
        for i in [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]]:
            next_map = check(office_map, r, c, i)
            solution(next_map, cameras, idx + 1)
    elif t == 5:
        next_map = check(office_map, r, c, [0, 1, 2, 3])
        solution(next_map, cameras, idx + 1)
    return


solution(office_map, cameras, 0)
print(answer)
