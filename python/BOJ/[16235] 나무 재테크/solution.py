N, M, K = [*map(int, input().split())]
A = [[*map(int, input().split())] for _ in range(N)]
trees = {(r, c): [] for r in range(N) for c in range(N)}
grounds = [[5]*N for _ in range(N)]
for _ in range(M):
    x, y, z = [*map(int, input().split())]
    trees[(x - 1, y - 1)].append(z)


def count_alive(trees):
    count = 0
    for ages in trees.values():
        count += len(ages)
    return count


def solution():
    global N, K
    global A, trees, grounds

    for _ in range(K):
        for season in ['spring', 'autumn', 'winter']:
            if season == 'spring':
                for (r, c), ages in trees.items():
                    ages.sort()
                    for idx, age in enumerate(ages):
                        if grounds[r][c] - age >= 0:
                            grounds[r][c] -= age
                            ages[idx] += 1
                        else:
                            deads = trees[(r, c)][idx:]
                            for dead in deads:
                                grounds[r][c] += (dead // 2)
                            trees[(r, c)] = trees[(r, c)][:idx]
                            break
            elif season == 'autumn':
                chk = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                       (1, 0), (1, -1), (0, -1), (-1, -1)]
                for (r, c), ages in trees.items():
                    for age in ages:
                        if age % 5 == 0:
                            for dr, dc in chk:
                                new_r, new_c = r + dr, c + dc
                                if 0 <= new_r < N and 0 <= new_c < N:
                                    trees[(new_r, new_c)].append(1)
            elif season == 'winter':
                for r in range(N):
                    for c in range(N):
                        grounds[r][c] += A[r][c]
    print(count_alive(trees))


solution()
