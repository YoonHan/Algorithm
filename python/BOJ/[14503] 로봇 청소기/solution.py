from sys import stdin
input = stdin.readline

N, M = list(map(int, input().split()))
x, y, d = list(map(int, input().split()))
board = [[*map(int, input().split())] for _ in range(N)]
ways = {0: [(0, -1, 3), (-1, 0, 0), (0, 1, 1), (1, 0, 2)],
        1: [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)],
        2: [(0, 1, 1), (1, 0, 2), (0, -1, 3), (-1, 0, 0)],
        3: [(1, 0, 2), (0, -1, 3), (-1, 0, 0), (0, 1, 1)]}    # 북 동 남 서


def chk_4_ways(x, y, ways):  # 사방 체크
    global board
    for way in ways:
        dx, dy = way[0], way[1]
        if board[x + dx][y + dy] == 0:
            return True
    return False


def back_possible(x, y, back):  # 사방이 막혀있느지 확인
    global board
    dx, dy, _ = back
    if board[x + dx][y + dy] != 1:
        return True
    return False


def solution():
    global N, M, x, y, d
    global board
    global ways
    count = 0
    cur_d = d
    is_finished = False

    while not is_finished:
        # 청소
        if board[x][y] == 0:
            board[x][y] = 'C'
            count += 1

        if chk_4_ways(x, y, ways[cur_d]):   # 사방 중에 청소할 곳이 남은 경우
            dx, dy, next_d = ways[cur_d][0]  # 현재 방향의 왼쪽 정보
            if board[x + dx][y + dy] == 0:
                x, y = x + dx, y + dy
                cur_d = next_d
            else:
                cur_d = next_d

        else:   # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
            if back_possible(x, y, ways[cur_d][-1]):   # 후진 가능하다면, 후진
                dx, dy, _ = ways[cur_d][-1]
                x, y = x + dx, y + dy
            else:
                is_finished = True
    print(count)


solution()
