def solution(m, n, board):
    answer = 0
    # preprocesssing
    board = list(map(list, board))
    # do while until there is no blocks to delete
    while True:
        # delete 4 consecutive blocks
        deleted = []
        for i in range(m - 1):  # find consecutive blocks
            for j in range(n - 1):
                now = board[i][j]
                if now == '0':
                    continue
                if board[i + 1][j] == now and board[i][j + 1] == now and board[i + 1][j + 1] == now:
                    if [i, j] not in deleted:
                        deleted.append([i, j])
                    if [i + 1, j] not in deleted:
                        deleted.append([i + 1, j])
                    if [i, j + 1] not in deleted:
                        deleted.append([i, j + 1])
                    if [i + 1, j + 1] not in deleted:
                        deleted.append([i + 1, j + 1])
        if len(deleted) == 0:
            break
        # delete
        answer += len(deleted)
        for i, j in deleted:
            board[i][j] = 0
        # and fill empty space
        board_T = []
        for col in zip(*board):
            col = list(
                ''.join([item for item in col if item != 0]).rjust(m, '0'))
            board_T.append(col)
        # undo transpose
        board = []
        for row in zip(*board_T):
            board.append(list(row))

    return answer
