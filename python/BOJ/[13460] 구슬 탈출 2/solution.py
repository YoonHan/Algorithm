import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [list(input())[:-1] for _ in range(N)]
visited_a = [[False]*M for _ in range(N)]
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)  # 동 남 서 북

def move(c, direction, ball):
  dst = 0
  x, y = c[0], c[1]
  while m[x+dx[direction]][y+dy[direction]] != '#' and m[x][y] != 'O':
    dst += 1
    x += dx[direction]
    y += dy[direction]
  return ((x, y), dst)


def solution():
  q = deque()
  ans = 0
  # init
  ri, bi = (0, 0), (0, 0)
  for i in range(N):
    for j in range(M):
      if m[i][j] == 'R': ri = (i, j)
      if m[i][j] == 'B': bi = (i, j)
  q.append([[ri, bi]])
  # logic
  while q:
    ans += 1
    if ans > 10: break
    next_candidates = []
    for rc, bc in q.popleft():
      for direction in range(len(dx)):
        next_rc, dst_rc = move(rc, direction, 'a')
        next_bc, dst_bc = move(bc, direction, 'b')
        if next_rc == next_bc and m[next_rc[0]][next_rc[1]] != 'O': # 같은 위치인지 체크
          if dst_rc > dst_bc: 
            next_rc = (next_rc[0]-dx[direction], next_rc[1]-dy[direction])
            dst_rc -= 1
          else: 
            next_bc = (next_bc[0]-dx[direction], next_bc[1]-dy[direction])
            dst_bc -= 1
        if m[next_bc[0]][next_bc[1]] == 'O': continue
        if m[next_rc[0]][next_rc[1]] == 'O': return ans
        if visited_a[next_rc[0]][next_rc[1]] == False: 
          visited_a[next_rc[0]][next_rc[1]] == True
          next_candidates.append([next_rc, next_bc])
    q.append(next_candidates)
  return -1

print(solution())