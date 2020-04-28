import sys
sys.setrecursionlimit(10000)

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


def dfs(r, c, united):
    global A, N, L, R
    global ways, board

    for dr, dc in ways:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == 0 and L <= abs(A[r][c] - A[nr][nc]) <= R:
                board[nr][nc] = 1
                united.append((nr, nc))
                dfs(nr, nc, united)
    return


def solution():
    global A
    global board
    is_fin = False
    count = 0

    while not is_fin:
        uniteds = []
        # DFS로 연합 구하기
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    united = []
                    dfs(r, c, united)
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
