from itertools import combinations

N, M = [*map(int, input().split())]
city = [[*map(int, input().split())] for _ in range(N)]
houses = []
chicken_houses = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_houses.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))


def get_city_chic_dist(chic_houses):
    global N, houses
    chic_dist_houses = []
    for hp in houses:
        hr, hc = hp[0], hp[1]
        chic_dist_house = []
        for cp in chic_houses:
            cr, cc = cp[0], cp[1]
            chic_dist_house.append(abs(hr - cr) + abs(hc - cc))
        chic_dist_houses.append(min(chic_dist_house))
    return sum(chic_dist_houses)


def solution():
    global M, city
    global chicken_houses
    dists = []
    # 치킨집 골라
    # 폐업시킨 뒤
    # 도시의 치킨거리 구하기
    for select_num in range(1, M + 1):
        for combi in combinations(chicken_houses, select_num):
            dists.append(get_city_chic_dist(combi))
    print(min(dists))


solution()
