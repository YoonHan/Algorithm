from collections import deque

N, L, R = list(map(int, input().split()))
A = [[*map(int, input().split())] for _ in range(N)]
ways = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 동 남 서 북
board = [[0]*N for _ in range(N)]


def get_avg(united):
    global A
    sums = 0
    for r, c in united:
        sums += A[r][c]
    return sums // len(united)


def bfs(r, c, united):
    global A, N, L, R
    global ways, board

    q = deque([(r, c)])
    while q:
        _r, _c = q.pop()
        for dr, dc in ways:
            nr, nc = _r + dr, _c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if L <= abs(A[nr][nc] - A[_r][_c]) <= R and board[nr][nc] == 0:
                    board[nr][nc] = 1
                    q.append((nr, nc))
                    united.append((nr, nc))
    return


def solution():
    global A
    global board
    is_fin = False
    count = 0

    while not is_fin:
        uniteds = []
        # BFS로 연합 구하기
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    united = []
                    bfs(r, c, united)
                    if len(united) != 0:
                        uniteds.append(united)
        # 연합이 없으면 종료 플래그 설정
        # 연합이 있으면 나머지 과정 수행
        if len(uniteds) == 0:
            is_fin = True
        else:
            for united in uniteds:
                avg = get_avg(united)
                for r, c in united:
                    A[r][c] = avg
            count += 1
            # 방문 정보 초기화
            board = [[0]*N for _ in range(N)]

    return count


print(solution())
