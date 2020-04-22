from sys import stdin
input = stdin.readline

N, M = [*map(int, input().split())]
board = [[*map(int, input().split())] for _ in range(N)]
max_val = -1
tetros = [[(0, 0), (0, 1), (0, 2), (0, 3)],  # 파랑 가로
          [(0, 0), (1, 0), (2, 0), (3, 0)],  # 파랑 세로
          [(0, 0), (0, 1), (1, 0), (1, 1)],  # 노랑
          [(0, 0), (1, 0), (2, 0), (2, 1)],  # 주황 기본
          [(0, 0), (0, 1), (0, 2), (1, 0)],  # 주황 90도
          [(0, 0), (0, 1), (1, 1), (2, 1)],  # 주황 180도
          [(0, 0), (1, 0), (1, -1), (1, -2)],  # 주황 270도
          [(0, 0), (0, 1), (-1, 1), (-2, 1)],  # 주황 기본 R
          [(0, 0), (0, 1), (0, 2), (1, 2)],  # 주황 90도 R
          [(0, 0), (0, 1), (1, 0), (2, 0)],  # 주황 180도 R
          [(0, 0), (1, 0), (1, 1), (1, 2)],  # 주황 270도 R
          [(0, 0), (1, 0), (1, 1), (2, 1)],  # 연두 기본
          [(0, 0), (0, 1), (1, 0), (1, -1)],  # 연두 90도
          [(0, 0), (1, 0), (1, -1), (2, -1)],  # 연두 기본 R
          [(0, 0), (0, 1), (1, 1), (1, 2)],  # 연두 90도 R
          [(0, 0), (0, 1), (0, 2), (1, 1)],  # 진분홍 기본
          [(0, 0), (1, 0), (1, -1), (2, 0)],  # 진분홍 90도
          [(0, 0), (1, -1), (1, 0), (1, 1)],  # 진분홍 기본 R
          [(0, 0), (1, 0), (2, 0), (1, 1)]]  # 진분홍 90도 R


def is_valid(x, y):
    if x == N or y == M: return False
    else: return True


def solution():
    global t
    global max_val
    for tetro in tetros:
        for i in range(N):
            for j in range(M):
                sum_result = 0
                for cell in tetro:
                    x, y = i + cell[0], j + cell[1]
                    if is_valid(x, y):
                        sum_result += board[i + cell[0]][j + cell[1]]
                    else: break
                max_val = max(max_val, sum_result)
    print(max_val)

solution()


