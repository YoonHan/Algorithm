from collections import defaultdict

N, K = list(map(int, input().split()))
board = [[*map(int, input().split())] for _ in range(N)]
chess_pieces = [[*map(int, input().split())] for _ in range(K)]


def solution():
    global N, K
    global board
    global chess_pieces
    turn = 0
    dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)  # 좌 우 상 하
    pieces = {}
    board_status = defaultdict(list)
    # 체스 말 순서 기억용 자료구조
    for idx, (r, c, d) in enumerate(chess_pieces):
        pieces[idx] = [r - 1, c - 1, d - 1, []]  # 행, 열, 방향, 업고있는 말 배열
    # 체스판 각 칸에 어떤 말이 있는지 기록
    for piece, (r, c, _, _) in pieces.items():
        board_status[(r, c)].append(piece)

    while True:
        turn += 1
        for order in range(K):
            r, c, d, ups = pieces[order]
            nr, nc = r + dr[d], c + dc[d]
            # 판을 벗어나거나 이동하려는 칸이 파란색인 경우
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                # 이동 방향 바꾸기
                if d == 0:
                    pieces[order][2] = 1
                    d = 1
                elif d == 1:
                    pieces[order][2] = 0
                    d = 0
                elif d == 2:
                    pieces[order][2] = 3
                    d = 3
                elif d == 3:
                    pieces[order][2] = 2
                    d = 2
                nr, nc = r + dr[d], c + dc[d]   # 이동할 칸 재정의
                # 판을 벗어나거나 이동하려는 곳이 파란색인 경우(아무것도 하지 않음)
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                    continue

            # 나머지 경우
            if board[nr][nc] == 0:  # 흰
                # 상태판 업데이트
                board_status[(nr, nc)] += ([order] + ups)
                for idx, piece in enumerate(board_status[(r, c)]):
                    if piece == order:
                        board_status[(r, c)] = board_status[(r, c)][:idx]
            elif board[nr][nc] == 1:    # 빨
                # 상태판 업데이트
                board_status[(nr, nc)] += reversed([order] + ups)
                for idx, piece in enumerate(board_status[(r, c)]):
                    if piece == order:
                        board_status[(r, c)] = board_status[(r, c)][:idx]

            # 말 위치 업데이트
            pieces[order][0], pieces[order][1] = nr, nc
            for upper in pieces[order][3]:
                pieces[upper][0], pieces[upper][1] = nr, nc
            # 쌓인 관계 업데이트
            for idx, piece in enumerate(board_status[(r, c)]):
                pieces[piece][3] = board_status[(r, c)][idx + 1:]
            for idx, piece in enumerate(board_status[(nr, nc)]):
                pieces[piece][3] = board_status[(nr, nc)][idx + 1:]

            # 4개가 쌓인 칸이 있는지 체크
            for coord, accu in board_status.items():
                if len(accu) >= 4:
                    print(turn)
                    exit()

        if turn > 1000:
            print(-1)
            break


solution()
