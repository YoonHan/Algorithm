from copy import deepcopy

T = int(input())
planes = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}
cube = [
    [['w', 'w', 'w'],   # 윗면
     ['w', 'w', 'w'],
     ['w', 'w', 'w']],
    [['y', 'y', 'y'],   # 아랫면
     ['y', 'y', 'y'],
     ['y', 'y', 'y']],
    [['r', 'r', 'r'],   # 앞 면
     ['r', 'r', 'r'],
     ['r', 'r', 'r']],
    [['o', 'o', 'o'],   # 뒷 면
     ['o', 'o', 'o'],
     ['o', 'o', 'o']],
    [['g', 'g', 'g'],    # 왼쪽 면
     ['g', 'g', 'g'],
     ['g', 'g', 'g']],
    [['b', 'b', 'b'],    # 오른쪽 면
     ['b', 'b', 'b'],
     ['b', 'b', 'b']]
]


def rotate_cube(commands):
    global cube
    global planes
    new_cube = deepcopy(cube)
    for command in commands:
        p, d = command[0], command[1]
        # 해당 면 회전
        p_n = planes[p]
        if d == '+':
            row = 0
            p_temp = deepcopy(new_cube[p_n])
            for c, b, a in zip(p_temp[0], p_temp[1], p_temp[2]):
                new_cube[p_n][row] = [a, b, c]
                row += 1

            if p == 'F':
                u, r, d, l = new_cube[planes['U']], new_cube[planes['R']], new_cube[planes['D']], new_cube[planes['L']]
                u_temp = u[2]
                u[2] = [l[2][2], l[1][2], l[0][2]]
                l[0][2], l[1][2], l[2][2] = d[0][0], d[0][1], d[0][2]
                d[0][0], d[0][1], d[0][2] = r[2][0], r[1][0], r[0][0]
                r[0][0], r[1][0], r[2][0] = u_temp
            elif p == 'B':
                u, r, d, l = new_cube[planes['U']], new_cube[planes['R']], new_cube[planes['D']], new_cube[planes['L']]
                u_temp = u[0]
                u[0] = [r[0][2], r[1][2], r[2][2]]
                r[0][2], r[1][2], r[2][2] = d[2][2], d[2][1], d[2][0]
                d[2][0], d[2][1], d[2][2] = l[0][0], l[1][0], l[2][0]
                l[0][0], l[1][0], l[2][0] = reversed(u_temp)
            elif p == 'U':
                f, r, b, l = new_cube[planes['F']], new_cube[planes['R']], new_cube[planes['B']], new_cube[planes['L']]
                f_temp = f[0]
                f[0] = r[0]
                r[0] = b[0]
                b[0] = l[0]
                l[0] = f_temp
            elif p == 'D':
                f, r, b, l = new_cube[planes['F']], new_cube[planes['R']], new_cube[planes['B']], new_cube[planes['L']]
                f_temp = f[2]
                f[2] = l[2]
                l[2] = b[2]
                b[2] = r[2]
                r[2] = f_temp
            elif p == 'L':
                u, f, d, b = new_cube[planes['U']], new_cube[planes['F']], new_cube[planes['D']], new_cube[planes['B']]
                u_temp = [u[0][0], u[1][0], u[2][0]]
                u[0][0], u[1][0], u[2][0] = b[2][2], b[1][2], b[0][2]
                b[0][2], b[1][2], b[2][2] = d[2][0], d[1][0], d[0][0]
                d[0][0], d[1][0], d[2][0] = f[0][0], f[1][0], f[2][0]
                f[0][0], f[1][0], f[2][0] = u_temp
            elif p == 'R':
                u, f, d, b = new_cube[planes['U']], new_cube[planes['F']], new_cube[planes['D']], new_cube[planes['B']]
                u_temp = [u[0][2], u[1][2], u[2][2]]
                u[0][2], u[1][2], u[2][2] = f[0][2], f[1][2], f[2][2]
                f[0][2], f[1][2], f[2][2] = d[0][2], d[1][2], d[2][2]
                d[0][2], d[1][2], d[2][2] = b[2][0], b[1][0], b[0][0]
                b[0][0], b[1][0], b[2][0] = reversed(u_temp)
        elif d == '-':
            row = 2
            p_temp = deepcopy(new_cube[p_n])
            for a, b, c in zip(p_temp[0], p_temp[1], p_temp[2]):
                new_cube[p_n][row] = [a, b, c]
                row -= 1

            if p == 'F':
                u, r, d, l = new_cube[planes['U']], new_cube[planes['R']], new_cube[planes['D']], new_cube[planes['L']]
                u_temp = u[2]
                u[2] = [r[0][0], r[1][0], r[2][0]]
                r[0][0], r[1][0], r[2][0] = d[0][2], d[0][1], d[0][0]
                d[0][0], d[0][1], d[0][2] = l[0][2], l[1][2], l[2][2]
                l[0][2], l[1][2], l[2][2] = reversed(u_temp)
            elif p == 'B':
                u, r, d, l = new_cube[planes['U']], new_cube[planes['R']], new_cube[planes['D']], new_cube[planes['L']]
                u_temp = u[0]
                u[0] = [l[2][0], l[1][0], l[0][0]]
                l[0][0], l[1][0], l[2][0] = d[2][0], d[2][1], d[2][2]
                d[2][0], d[2][1], d[2][2] = r[2][2], r[1][2], r[0][2]
                r[0][2], r[1][2], r[2][2] = u_temp
            elif p == 'U':
                f, r, b, l = new_cube[planes['F']], new_cube[planes['R']], new_cube[planes['B']], new_cube[planes['L']]
                f_temp = f[0]
                f[0] = l[0]
                l[0] = b[0]
                b[0] = r[0]
                r[0] = f_temp
            elif p == 'D':
                f, r, b, l = new_cube[planes['F']], new_cube[planes['R']], new_cube[planes['B']], new_cube[planes['L']]
                f_temp = f[2]
                f[2] = r[2]
                r[2] = b[2]
                b[2] = l[2]
                l[2] = f_temp
            elif p == 'L':
                u, f, d, b = new_cube[planes['U']], new_cube[planes['F']], new_cube[planes['D']], new_cube[planes['B']]
                u_temp = [u[0][0], u[1][0], u[2][0]]
                u[0][0], u[1][0], u[2][0] = f[0][0], f[1][0], f[2][0]
                f[0][0], f[1][0], f[2][0] = d[0][0], d[1][0], d[2][0]
                d[0][0], d[1][0], d[2][0] = b[2][2], b[1][2], b[0][2]
                b[0][2], b[1][2], b[2][2] = reversed(u_temp)
            elif p == 'R':
                u, f, d, b = new_cube[planes['U']], new_cube[planes['F']], new_cube[planes['D']], new_cube[planes['B']]
                u_temp = [u[0][2], u[1][2], u[2][2]]
                u[0][2], u[1][2], u[2][2] = b[2][0], b[1][0], b[0][0]
                b[0][0], b[1][0], b[2][0] = d[2][2], d[1][2], d[0][2]
                d[0][2], d[1][2], d[2][2] = f[0][2], f[1][2], f[2][2]
                f[0][2], f[1][2], f[2][2] = u_temp
    return new_cube


def print_top(cube):
    for row in cube[0]:
        for col in row:
            print(col, end='')
        print()


def solution():
    global T
    for _ in range(T):
        _ = int(input())
        commands = [(case[0], case[1]) for case in input().split()]
        new_cube = rotate_cube(commands)
        print_top(new_cube)


solution()
