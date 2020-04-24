N, L = [*map(int, input().split())]
m = [[*map(int, input().split())]for _ in range(N)]


def chk_climb_col(r, c, l, cr):
    global N, m
    is_possible = True
    height = m[r][c]
    r_locs = []

    for i in range(l):
        if c - i < 0 or height != m[r][c - i] or cr[c - i] == 1:
            is_possible = False
            break
        else:
            r_locs.append(c - i)

    if is_possible:
        for loc in r_locs:
            cr[loc] = 1
        return is_possible
    else:
        return is_possible


def chk_down_col(r, c, l, cr):
    global N, m
    is_possible = True
    height = m[r][c + 1]
    r_locs = []

    for i in range(1, l + 1):
        if c + i >= N or height != m[r][c + i] or cr[c + i] == 1:
            is_possible = False
            break
        else:
            r_locs.append(c + i)

    if is_possible:
        for loc in r_locs:
            cr[loc] = 1
        return is_possible
    else:
        return is_possible


def chk_climb_row(r, c, l, cr):
    global N, m
    is_possible = True
    height = m[r][c]
    r_locs = []

    for i in range(l):
        if r - i < 0 or height != m[r - i][c] or cr[r - i] == 1:
            is_possible = False
            break
        else:
            r_locs.append(r - i)

    if is_possible:
        for loc in r_locs:
            cr[loc] = 1
        return is_possible
    else:
        return is_possible


def chk_down_row(r, c, l, cr):
    global N, m
    is_possible = True
    height = m[r + 1][c]
    r_locs = []

    for i in range(1, l + 1):
        if r + i >= N or height != m[r + i][c] or cr[r + i] == 1:
            is_possible = False
            break
        else:
            r_locs.append(r + i)

    if is_possible:
        for loc in r_locs:
            cr[loc] = 1
        return is_possible
    else:
        return is_possible


def solution():
    global N, L
    global m
    possible = 0

    # 가로로 놓인 길들 검사
    for r in range(N):
        chk_road = [0] * N
        for c in range(N):
            if c == N - 1:
                possible += 1
                break
            height_diff = abs(m[r][c] - m[r][c + 1])
            if height_diff == 1:  # 경사로를 놓는다
                if m[r][c] < m[r][c + 1]:  # 오르막
                    if not chk_climb_col(r, c, L, chk_road):
                        break
                elif m[r][c] > m[r][c + 1]:  # 내리막
                    if not chk_down_col(r, c, L, chk_road):
                        break
            elif height_diff >= 2:   # 불가능한 길
                break

    # 세로로 놓인 길들 검사
    for c in range(N):
        chk_road = [0] * N
        for r in range(N):
            if r == N - 1:
                possible += 1
                break
            height_diff = abs(m[r][c] - m[r + 1][c])
            if height_diff == 1:  # 경사로를 놓는다
                if m[r][c] < m[r + 1][c]:  # 오르막
                    if not chk_climb_row(r, c, L, chk_road):
                        break
                elif m[r][c] > m[r + 1][c]:  # 내리막
                    if not chk_down_row(r, c, L, chk_road):
                        break
            elif height_diff >= 2:  # 불가능한 길
                break
    print(possible)


solution()
