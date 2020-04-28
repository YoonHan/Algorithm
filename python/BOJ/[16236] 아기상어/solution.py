from collections import deque

N = int(input())
space = [[*map(int, input().split())] for _ in range(N)]


def bfs(sr, sc, size, visited):
    global N, space
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서
    visited[sr][sc] = 1
    preys = []
    shortest = 99999
    stop = False
    q = deque([(sr, sc, 0)])

    while q:
        r, c, d = q.popleft()
        if stop and shortest < d:
            break
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if space[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc, d + 1))
                elif space[nr][nc] == size and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc, d + 1))
                elif 0 < space[nr][nc] < size:
                    if (nr, nc, d + 1) not in preys:
                        preys.append((nr, nc, d + 1))
                        shortest = d
                        stop = True
    if len(preys) == 0:
        return -1, -1, 0
    else:
        preys.sort(key=lambda x: (x[0], x[1]))
        pr, pc, lapsed = preys[0]
        space[sr][sc] = 0
        space[pr][pc] = 9
        return pr, pc, lapsed


def solution():
    global space
    sr, sc = (-1, -1)
    eaten = 0
    size = 2
    is_fin = False
    answer = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                sr, sc = (i, j)

    while not is_fin:
        copy_visited = [line[:] for line in visited]
        next_sr, next_sc, lapsed = bfs(sr, sc, size, copy_visited)
        if next_sr == -1 and next_sc == -1:   # 먹이를 못찾은 경우
            is_fin = True
        else:
            if size == 14: break
            sr, sc = next_sr, next_sc
            eaten += 1
            answer += lapsed
            if eaten == size and size < 9:
                size += 1
                eaten = 0
    print(answer)


solution()
