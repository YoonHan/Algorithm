from sys import stdin
from math import inf
from itertools import permutations
input = stdin.readline

N = int(input())
numbers = [*map(int, input().strip().split())]
counts = [*map(int, input().strip().split())]
max_val = -inf
min_val = inf


def calc(nums, ops): # 숫자배열과 연산자 배열을 주면 결과 값 계산
    res = nums[0]
    for idx, op in enumerate(ops):
        if op == '+':
            res += nums[idx + 1]
        elif op == '-':
            res -= nums[idx + 1]
        elif op == '*':
            res *= nums[idx + 1]
        elif op == '/':
            if res < 0: res = -((-res) // nums[idx + 1])
            else: res = res // nums[idx + 1]
    return res


def get_ops(cnts):  # 각 연산자의 개수에 대한 배열을 주면 그에 대응하는 연산자 배열 돌려줌
    _ops = []
    for idx, c in enumerate(cnts):
        if idx == 0: _ops += ['+'] * c
        elif idx == 1: _ops += ['-'] * c
        elif idx == 2: _ops += ['*'] * c
        elif idx == 3: _ops += ['/'] * c
    return _ops


def get_permu(ops):
    if len(ops) == 1: return ops
    else: return list(set(permutations(ops)))


def solution():
    global numbers, counts
    global max_val, min_val

    ops_permu = get_permu(get_ops(counts))
    for op in ops_permu:
        result = calc(numbers, op)
        max_val = max(result, max_val)
        min_val = min(result, min_val)
    print(max_val)
    print(min_val)


solution()
