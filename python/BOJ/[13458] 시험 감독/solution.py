from sys import stdin
input = stdin.readline

N = int(input())
people = list(map(int, input().split()))
main, sub = list(map(int, input().split()))


def solution():
    total = 0
    for p in people:
        if p // main == 0:
            total += 1
            continue
        else:
            p -= main
            total += 1
            sub_q, sub_r = p // sub, p % sub
            total += sub_q
            if sub_r > 0:
                total += 1
    return total


print(solution())
