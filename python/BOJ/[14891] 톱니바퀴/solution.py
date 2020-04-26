from collections import deque

gears = []
moves = []
for _ in range(4):
    dq = deque([*map(int, list(input()))])
    gears.append(dq)
for _ in range(int(input())):
    moves.append([*map(int, input().split())])


def get_score(gears):
    res = 0
    for idx, gear in enumerate(gears):
        if gear[0] == 1:
            res += (2**idx)
    return res


def rotate(gears, which, dir):
    neighbors = []
    if which == 0:
        for i in range(3):
            if gears[i][2] != gears[i + 1][6]:
                neighbors.append(i + 1)
            else:
                break
        gears[0].rotate(dir)
        for idx, neighbor in enumerate(neighbors):
            gears[neighbor].rotate(dir * ((-1)**(idx + 1)))
    elif which == 1:
        if gears[1][6] != gears[0][2]:
            gears[0].rotate(-dir)
        for i in range(1, 3):
            if gears[i][2] != gears[i + 1][6]:
                neighbors.append(i + 1)
            else:
                break
        gears[1].rotate(dir)
        for idx, neighbor in enumerate(neighbors):
            gears[neighbor].rotate(dir * ((-1)**(idx + 1)))
    elif which == 2:
        if gears[2][2] != gears[3][6]:
            gears[3].rotate(-dir)
        for i in range(2, 0, -1):
            if gears[i][6] != gears[i - 1][2]:
                neighbors.append(i - 1)
            else:
                break
        gears[2].rotate(dir)
        for idx, neighbor in enumerate(neighbors):
            gears[neighbor].rotate(dir * ((-1) ** (idx + 1)))
    elif which == 3:
        for i in range(3, 0, -1):
            if gears[i][6] != gears[i - 1][2]:
                neighbors.append(i - 1)
            else:
                break
        gears[3].rotate(dir)
        for idx, neighbor in enumerate(neighbors):
            gears[neighbor].rotate(dir * ((-1)**(idx + 1)))


def solution(gears, moves):
    for move in moves:
        which = move[0] - 1     # 0 1 2 3 번 톱니
        dir = move[1]
        rotate(gears, which, dir)
    return get_score(gears)


print(solution(gears, moves))
