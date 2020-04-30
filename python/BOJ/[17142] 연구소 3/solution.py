from itertools import combinations
from collections import deque

N, M = list(map(int, input().split()))
lab = [[*map(int, input().split())] for _ in range(N)]


def check(_lab):
    global N
    lapsed = 0
    for r in range(N):
        for c in range(N):
            if _lab[r][c] == 0:
                return -1
            elif _lab[r][c] != 'Y' and _lab[r][c] != 'N' and _lab[r][c] != '-':
                lapsed = max(lapsed, _lab[r][c])
    return lapsed


def bfs(virus_locs, _lab):
    dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)   # 동 남 서 북
    for r, c, _ in virus_locs:
        _lab[r][c] = 'Y'
    q = deque(virus_locs)
    while q:
        r, c, d = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if _lab[nr][nc] == 0:   # 빈 칸에 전파
                    _lab[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))
                elif _lab[nr][nc] == 'N':   # 비활성 -> 활성
                    _lab[nr][nc] = 'Y'
                    q.append((nr, nc, d + 1))
    return check(_lab)


def solution():
    global N, M, lab
    viruses = []
    answers = []    # 각 조합별 결과 저장
    # 바이러스 위치 기록
    for r in range(N):
        for c in range(N):
            if lab[r][c] == 2:
                lab[r][c] = 'N'
                viruses.append((r, c, 0))
    # 맵 표시 변환
    for r in range(N):
        for c in range(N):
            if lab[r][c] == 1:
                lab[r][c] = '-'
    # M 개 골라서 활성화 시키고 전파시키기
    for virus_locs in combinations(viruses, M):
        _lab = [line[:] for line in lab]
        answers.append(bfs(virus_locs, _lab))
    # 정답 출력
    if all(item == -1 for item in answers):
        print(-1)
    else:
        candidates = []
        for candidate in answers:
            if candidate != -1:
                candidates.append(candidate)
        print(min(candidates))


solution()
