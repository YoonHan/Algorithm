dice_nums = list(map(int, input().split()))
# 0: 시작, 끝
# 각 key 는 path 의 유형을 나타냄
board = {0: [n for n in range(0, 42, 2)] + [0],
         1: [10, 13, 16, 19, 25, 30, 35, 40, 0],
         2: [20, 22, 24, 25, 30, 35, 40, 0],
         3: [30, 28, 27, 26, 25, 30, 35, 40, 0]}
answer = 0


def move(cur_piece, pieces, score, depth):
    global dice_nums
    global board
    num_moves = dice_nums[depth]
    cur_path = pieces[cur_piece][0]
    cur_idx = pieces[cur_piece][1]

    # 판의 끝에 도달하는지 체크
    next_idx = cur_idx + num_moves
    road_len = len(board[cur_path])
    if next_idx >= road_len - 1:
        pieces[cur_piece][1] = road_len - 1
        return score, True, True
    # 이동하려고 하는 곳에 말이 있으면 이동하지 않는다.
    for other_piece, info in pieces.items():
        if cur_piece != other_piece:    # 자신과의 비교는 하지 않는다
            # 같은 유형의 길에서, 도달하려고 하는 위치에 다른 말이 놓인 경우.
            if cur_path == info[0] and next_idx == info[1]:
                return -1, False, False
            # 각 유형의 길마다 예외처리
            if cur_path == 0:   # 0번 길
                if (next_idx == 5 * info[0]) and info[1] == 0:  # 5, 10, 15번 칸
                    return -1, False, False
                if next_idx == road_len - 2:  # 40번 칸
                    if (info[0] == 1 or info[0] == 3) and info[1] == 7:
                        return -1, False, False
                    if info[0] == 2 and info[1] == 6:
                        return -1, False, False
            if cur_path == 1:   # 1번 길
                if info[0] == 2 and (next_idx - 1 == info[1]):  # 2번 길과 중복체크
                    return -1, False, False
                if info[0] == 3 and (next_idx == info[1]):  # 3번 길과 중복체크
                    return -1, False, False
                # 0번 길과 중복체크
                if info[0] == 0 and info[1] == 20 and (next_idx == road_len - 2):
                    return -1, False, False
            if cur_path == 2:   # 2번 길
                if (info[0] == 1 or info[0] == 3) and (next_idx + 1 == info[1]):  # 1, 3번 길과 중복체크
                    return -1, False, False
                # 0번 길과 중복체크
                if info[0] == 0 and info[1] == 20 and (next_idx == road_len - 2):
                    return -1, False, False
            if cur_path == 3:   # 3번 길
                if info[0] == 1 and next_idx == info[1]:  # 1번 길과 중복체크
                    return -1, False, False
                if info[0] == 2 and (next_idx - 1 == info[1]):  # 2번 길과 중복체크
                    return -1, False, False
                # 0번 길과 중복체크
                if info[0] == 0 and info[1] == 20 and (next_idx == road_len - 2):
                    return -1, False, False
    # 이동 시키기
    pieces[cur_piece][1] = next_idx
    # 점수 누적
    score += board[cur_path][pieces[cur_piece][1]]
    # 교차로 체크
    if cur_path == 0:
        if pieces[cur_piece][1] == 5:
            pieces[cur_piece][0], pieces[cur_piece][1] = 1, 0
        elif pieces[cur_piece][1] == 10:
            pieces[cur_piece][0], pieces[cur_piece][1] = 2, 0
        elif pieces[cur_piece][1] == 15:
            pieces[cur_piece][0], pieces[cur_piece][1] = 3, 0

    return score, True, False


def dfs(cur_piece, pieces, score, depth, excep):
    global dice_nums, answer
    if depth == 10:
        answer = max(answer, score)
        return

    # 선택한 말 이동시키기
    next_score, can_move, is_fin = move(cur_piece, pieces, score, depth)
    # 이동하려는 칸에 말이 있는 경우 이동하지 않고 그대로 반환
    if not can_move:
        return
    if is_fin:
        excep.append(cur_piece)
    # DFS
    for next_piece in range(1, 5):
        next_pieces = {k: v[:] for k, v in pieces.items()}
        if next_piece not in excep:
            next_excep = excep[:]
            dfs(next_piece, next_pieces, next_score, depth + 1, next_excep)

    return


def solution():
    for start in range(1, 5):
        # {말 번호: (놓여 있는 길 유형, 길 위에서의 인덱스)}
        pieces = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0]}
        excep = []
        dfs(start, pieces, 0, 0, excep)
    print(answer)


solution()
