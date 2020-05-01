from collections import defaultdict

R, C, T = list(map(int, input().split()))
A = [[*map(int, input().split())] for _ in range(R)]


def get_dust_amount():
    global A, R, C
    sums = 0
    for r in range(R):
        for c in range(C):
            if A[r][c] != -1 and A[r][c] != 0:
                sums += A[r][c]
    return sums


def solution():
    global R, C, T, A
    # 공기 청정기 좌표
    air_puri = []   # 순서대로 위 아래
    dr, dc = (0, -1, 0, 1), (1, 0, -1, 0)   # 동 북 서 남
    upper_blows = []
    lower_blows = []
    for r in range(R):
        for c in range(C):
            if A[r][c] == -1:
                air_puri.append((r, c))
    # 바람 방향 기록
    for idx, (ar, ac) in enumerate(air_puri):
        # 위쪽
        if idx == 0:    # 0 1 2 3 -> 동 북 서 남
            for col_right in range(ac + 1, C - 1):
                upper_blows.append((ar, col_right, 0))
            for row_up in range(ar, 0, -1):
                upper_blows.append((row_up, C - 1, 1))
            for col_left in range(C - 1, 0, -1):
                upper_blows.append((0, col_left, 2))
            for row_down in range(0, ar):
                upper_blows.append((row_down, 0, 3))
            for col_right in range(0, ac):
                upper_blows.append((ar, col_right, 0))
        # 아래쪽
        else:
            for col_right in range(ac + 1, C - 1):
                lower_blows.append((ar, col_right, 0))
            for row_down in range(ar, R - 1):
                lower_blows.append((row_down, C - 1, 3))
            for col_left in range(C - 1, 0, -1):
                lower_blows.append((R - 1, col_left, 2))
            for row_up in range(R - 1, ar, -1):
                lower_blows.append((row_up, 0, 1))
            for col_right in range(0, ac):
                lower_blows.append((ar, col_right, 0))
    # T 초간 수행
    for _ in range(T):
        after = defaultdict(list)
        # 칸마다 돌면서 확산 정보 after에 저장
        for r in range(R):
            for c in range(C):
                amount = A[r][c]
                spread = amount // 5
                if amount != 0 and amount != -1:    # 미세먼지가 존재하는 칸
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                            after[(nr, nc)].append(spread)
                            amount -= spread
                    after[(r, c)].append(amount)
        # after에 저장된 정보 처리
        for (r, c), values in after.items():
            A[r][c] = sum(values)
        # 바람따라 이동시키기
        for idx in range(len(upper_blows) - 1, -1, -1):
            if idx == len(upper_blows) - 1:
                continue
            r, c, d = upper_blows[idx]
            nr, nc = r + dr[d], c + dc[d]
            A[nr][nc] = A[r][c]
            A[r][c] = 0
        for idx in range(len(lower_blows) - 1, -1, -1):
            if idx == len(lower_blows) - 1:
                continue
            r, c, d = lower_blows[idx]
            nr, nc = r + dr[d], c + dc[d]
            A[nr][nc] = A[r][c]
            A[r][c] = 0

    print(get_dust_amount())


solution()
