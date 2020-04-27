N = int(input())
curves = [[*map(int, input().split())] for _ in range(N)]
board = [[0 for _ in range(101)] for _ in range(101)]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)


def make_dragon_curve(curve):
    # 0 세대 만들기
    x, y, d, g = curve
    dragon_curve = []
    dragon_curve.append((x, y))
    dragon_curve.append((x + dx[d], y + dy[d]))

    # 나머지 세대 만들기
    for _ in range(g):
        last = dragon_curve[-1]
        rest = dragon_curve[:-1]
        new = []
        for r in rest:
            _dx, _dy = r[0] - last[0], r[1] - last[1]
            new.insert(0, (last[0] + (-_dy), last[1] + _dx))
        dragon_curve += new
    return dragon_curve


def record(dc):
    global board
    for point in dc:
        x, y = point[0], point[1]
        board[y][x] = 1


def count_square():
    global board
    count = 0
    for x in range(100):
        for y in range(100):
            if board[y][x] == 1 and board[y][x + 1] == 1 and \
               board[y + 1][x] == 1 and board[y + 1][x + 1] == 1:
                count += 1
    return count


def solution():
    global N
    global curves

    for curve in curves:
        dc = make_dragon_curve(curve)
        record(dc)
    return count_square()


print(solution())
