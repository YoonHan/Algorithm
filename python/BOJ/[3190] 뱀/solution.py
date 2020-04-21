# 라이브러리 로드
from collections import deque

# 입력 받기
N = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
L = int(input())
rot = [input().split() for _ in range(L)]
for item in rot:
    item[0] = int(item[0])

# 초기화
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
m = [[0 for _ in range(N)] for _ in range(N)]
d_m = [[-1 for _ in range(N)] for _ in range(N)]
for a_x, a_y in apples:
    m[a_x - 1][a_y - 1] = 1

# 로직


def chk_finished(h_x, h_y, body):
    global N
    if (h_x <= -1 or h_x >= N) or (h_y <= -1 or h_y >= N):
        return True
    for b_x, b_y in body:
        if h_x == b_x and h_y == b_y:
            return True
    return False


def move(body):
    new_body = []
    for part in body:
        x, y = part
        new_part = (x+dx[d_m[x][y]], y+dy[d_m[x][y]])
        new_body.append(new_part)
    return new_body
    print('new body: ', new_body)


def solution():
    t_lapsed = 0
    h_x, h_y = (0, 0)
    body = [(0, 0)]     # 처음에 꼬리 좌표만 저장
    rot_q = deque(rot)
    cur_d_q = deque([i for i in range(len(dx))])
    next_rot_time, next_rot = rot_q.popleft()
    while True:
        t_lapsed += 1   # 시간 경과시키고
        cur_d = cur_d_q.popleft()   # 머리의 진행방향 꺼내기
        d_m[h_x][h_y] = cur_d     # 맵에 진행방향 기록
        h_x, h_y = h_x + dx[cur_d], h_y + dy[cur_d]  # 머리 움직이기
        cur_d_q.appendleft(cur_d)   # 머리의 진행방향 다시 넣기
        t_x, t_y = body[-1]  # 꼬리 생성할 좌표 저장

        if chk_finished(h_x, h_y, body):
            break   # 갱신된 좌표로 게임 상태 체크
        body = move(body)   # 꼬리포함 몸체 이동

        if m[h_x][h_y] == 1:  # 사과 확인
            m[h_x][h_y] = 0
            body.append((t_x, t_y))

        if next_rot_time == t_lapsed:  # 진행방향을 바꿀 시간이면
            if next_rot == 'L':
                cur_d_q.rotate(1)
            elif next_rot == 'D':
                cur_d_q.rotate(-1)
            if rot_q:
                next_rot_time, next_rot = rot_q.popleft()

    print(t_lapsed)


solution()
