N = int(input())
S = [[*map(int, input().split())] for _ in range(N)]
min_value = 99999


def calc_ability(team):
    global S
    comb = combinations(team, 2)
    ability = 0
    for x, y in comb:
        ability += S[x][y] + S[y][x]
    return ability


def combinations(lst, n):
    comb = []
    l = len(lst)
    if l < n:
        return []
    if l == 0:
        return []
    if l == 1:
        return [lst]

    if n == 1:
        for item in lst:
            comb.append([item])
        return comb

    # more than 1 element in lst
    for i in range(len(lst)):
        head = lst[i]
        rem_lst = lst[i + 1:]
        for c in combinations(rem_lst, n - 1):
            comb.append([head] + c)
    return comb


def solution():
    global N, S
    global min_value
    players = [i for i in range(N)]
    combs = combinations(players, N // 2)
    players = set(players)
    combs = [c for c in combs if c[0] == 0]

    for c in combs:
        start = set(c)
        link = players - set(c)
        start_ability = calc_ability(list(start))
        link_ability = calc_ability(list(link))
        min_value = min(min_value, abs(start_ability - link_ability))
    print(min_value)


solution()
