from sys import stdin
from copy import deepcopy
from collections import deque
input = stdin.readline

N, M, x, y, k = [*map(int, input().split())]
board = [[*map(int, input().split())] for _ in range(N)]
command = [*map(int, input().split())]
way = [1, 2, 3, 4]  # 동 서 북 남
dice = {'top': 0, 'bottom': 0,
        'front': 0, 'back': 0,
        'left': 0, 'right': 0}


def roll(dice, way):
    new_dice = deepcopy(dice)
    global x, y
    if way == 1:    # 동
        new_dice['bottom'] = dice['right']
        new_dice['left'] = dice['bottom']
        new_dice['top'] = dice['left']
        new_dice['right'] = dice['top']
        y += 1
    elif way == 2:  # 서
        new_dice['bottom'] = dice['left']
        new_dice['left'] = dice['top']
        new_dice['top'] = dice['right']
        new_dice['right'] = dice['bottom']
        y -= 1
    elif way == 3:  # 북
        new_dice['top'] = dice['front']
        new_dice['bottom'] = dice['back']
        new_dice['front'] = dice['bottom']
        new_dice['back'] = dice['top']
        x -= 1
    elif way == 4:  # 남
        new_dice['top'] = dice['back']
        new_dice['bottom'] = dice['front']
        new_dice['front'] = dice['top']
        new_dice['back'] = dice['bottom']
        x += 1
    return new_dice


def look_up(next):
    if next == 1:
        if y + 1 >= M:
            return False
        else:
            return True
    elif next == 2:
        if y - 1 <= -1:
            return False
        else:
            return True
    elif next == 3:
        if x - 1 <= -1:
            return False
        else:
            return True
    elif next == 4:
        if x + 1 >= N:
            return False
        else:
            return True


def solution():
    global dice
    global board
    q = deque(command)
    while q:
        next = q.popleft()
        if look_up(next):
            dice = roll(dice, next)
            if board[x][y] == 0:
                board[x][y] = dice['bottom']
                print(dice['top'])
            else:
                dice['bottom'] = board[x][y]
                board[x][y] = 0
                print(dice['top'])
        else:
            continue


solution()
