from sys import stdin
input = stdin.readline

N, M = list(map(int, input().split()))
board = [[*map(int, input().split())] for _ in range(N)]
max_size = 0

# 1. 기둥 골라 세우기(3곳)
# 2. 바이러스 전파시키기(DFS)
# 3. 빈칸세서 안전영역 크기 업데이트
# 4. 1 ~ 3 반복


def dfs(r, c):
    global N, M
    global board
    if board[r][c] == 0:    # 빈 칸이면 전파
        board[r][c] = 2
    # DFS
    if r + 1 <= N - 1 and board[r + 1][c] == 0:
        dfs(r + 1, c)
    if r - 1 >= 0 and board[r - 1][c] == 0:
        dfs(r - 1, c)
    if c + 1 <= M - 1 and board[r][c + 1] == 0:
        dfs(r, c + 1)
    if c - 1 >= 0 and board[r][c - 1] == 0:
        dfs(r, c - 1)
    return


def spread(viruses):
    for virus in viruses:
        dfs(virus[0], virus[1])


def count_safety_zone(board):
    count = 0
    for row in board:
        for item in row:
            if item == 0:
                count += 1
    return count


def solution():
    global N, M
    global max_size
    global board
    empty = []
    viruses = []

    # 빈 칸과 바이러스 좌표 저장
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                empty.append((row, col))
            elif board[row][col] == 2:
                viruses.append((row, col))

    restore = [line[:] for line in board]    # 추후 보드 복원
    # 기둥 3개 고르고
    # 전파시키고
    # 안전 구역 계산
    empty_num = len(empty)
    for i in range(empty_num):
        for j in range(i + 1, empty_num):
            for k in range(j + 1, empty_num):
                board[empty[i][0]][empty[i][1]] = 1
                board[empty[j][0]][empty[j][1]] = 1
                board[empty[k][0]][empty[k][1]] = 1
                spread(viruses)
                max_size = max(max_size, count_safety_zone(board))
                board = [line[:] for line in restore]


solution()
print(max_size)
