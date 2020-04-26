from itertools import combinations

N, M, H = [*map(int, input().split())]  # N = 세로선, M = 가로선
ladders = [[*map(int, input().split())] for _ in range(M)]
ladder_map = [[0 for _ in range(N - 1)] for _ in range(H)]
empty_points = []

# 초기 사다리 위치 기록
for point in ladders:
    r = point[0] - 1
    ladder_map[r][point[1] - 1] = 1

# 사다리가 없는 위치 기록
for row, dotted in enumerate(ladder_map):
    for col, point in enumerate(dotted):
        if point == 0:
            empty_points.append((row, col))


def play(ladder_map):
    global N, H

    for i in range(N):
        start = [0, i]
        while start[0] < H:
            r, c = start[0], start[1]
            # 사다리 지점에서 왼쪽 또는 오른쪽으로 이동
            if c - 1 >= 0 and ladder_map[r][c - 1] == 1:
                start[1] -= 1
            elif c <= N - 2 and ladder_map[r][c] == 1:
                start[1] += 1
            # 내려가기
            start[0] += 1

        # 각 지점의 끝난 지점이 자기 자신이 아니면 실패
        if start[1] != i:
            return False

    return True


def simulate(num_ladder):
    global N
    global ladder_map
    global empty_points

    for combination in combinations(empty_points, num_ladder):
        new_ladder_map = [line[:] for line in ladder_map]
        is_possible_case = True
        # 사다리 추가
        for point in combination:
            r, c = point[0], point[1]
            if (c - 1 < 0 or (c - 1 >= 0 and new_ladder_map[r][c - 1] == 0)) and \
               (c + 1 >= N - 1 or (c + 1 <= N - 2 and new_ladder_map[r][c + 1] == 0)):
                new_ladder_map[r][c] = 1
            else:
                is_possible_case = False
        # 시뮬레이션
        if is_possible_case:
            if play(new_ladder_map):
                return True
    return False


def solution():
    global M
    answer = -1
    if M == 0:
        return 0

    # 사다리를 0개, 1개, 2개.. 씩 놓아보면서
    # 가능한지 체크
    for add in range(4):
        if simulate(add):
            answer = add
            break
    return answer


print(solution())
