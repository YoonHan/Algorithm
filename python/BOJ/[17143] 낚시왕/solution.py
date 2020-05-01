from collections import defaultdict, deque

R, C, M = list(map(int, input().split()))
sharks = [[*map(int, input().split())] for _ in range(M)]


def solution():
    # 1 2 3 4 -> 상 하 우 좌
    global R, C, M
    global sharks
    picked = []
    shark_maps = defaultdict(deque)
    for (r, c, s, d, z) in sharks:
        shark_maps[(r, c)].append((s, d, z))

    pos = 0
    while pos < C:
        # 낚시꾼 이동
        pos += 1
        # 상어 잡기
        candidates = list(shark_maps.keys())
        candidates.sort(key=lambda x: (x[1], x[0]))
        for r, c in candidates:
            if pos == c:
                _, _, size = shark_maps[(r, c)].pop()
                del(shark_maps[(r, c)])
                picked.append(size)
                break
        # 상어 이동
        next_shark_maps = defaultdict(deque)
        for (r, c), shark in shark_maps.items():
            s, d, z = list(shark)[0]
            if d == 1:  # 상
                if r - s < 1:   # 방향 전환
                    rest = r - 1
                    togo = s - rest
                    quo, rem = togo // (R - 1), togo % (R - 1)
                    if quo % 2 == 0:
                        if rem == 0:
                            next_shark_maps[(1, c)].append((s, d, z))
                        else:
                            next_shark_maps[(1 + rem, c)].append((s, 2, z))
                    else:
                        if rem == 0:
                            next_shark_maps[(R, c)].append((s, 2, z))
                        else:
                            next_shark_maps[(R - rem, c)].append((s, d, z))
                else:
                    next_shark_maps[(r - s, c)].append((s, d, z))
            elif d == 2:    # 하
                if r + s > R:
                    rest = R - r
                    togo = s - rest
                    quo, rem = togo // (R - 1), togo % (R - 1)
                    if quo % 2 == 0:
                        if rem == 0:
                            next_shark_maps[(R, c)].append((s, d, z))
                        else:
                            next_shark_maps[(R - rem, c)].append((s, 1, z))
                    else:
                        if rem == 0:
                            next_shark_maps[(1, c)].append((s, 1, z))
                        else:
                            next_shark_maps[(1 + rem, c)].append((s, d, z))
                else:
                    next_shark_maps[(r + s, c)].append((s, d, z))
            elif d == 3:    # 우
                if c + s > C:
                    rest = C - c
                    togo = s - rest
                    quo, rem = togo // (C - 1), togo % (C - 1)
                    if quo % 2 == 0:
                        if rem == 0:
                            next_shark_maps[(r, C)].append((s, d, z))
                        else:
                            next_shark_maps[(r, C - rem)].append((s, 4, z))
                    else:
                        if rem == 0:
                            next_shark_maps[(r, 1)].append((s, 4, z))
                        else:
                            next_shark_maps[(r, 1 + rem)].append((s, d, z))
                else:
                    next_shark_maps[(r, c + s)].append((s, d, z))
            elif d == 4:    # 좌
                if c - s < 1:
                    rest = c - 1
                    togo = s - rest
                    quo, rem = togo // (C - 1), togo % (C - 1)
                    if quo % 2 == 0:
                        if rem == 0:
                            next_shark_maps[(r, 1)].append((s, d, z))
                        else:
                            next_shark_maps[(r, 1 + rem)].append((s, 3, z))
                    else:
                        if rem == 0:
                            next_shark_maps[(r, C)].append((s, 3, z))
                        else:
                            next_shark_maps[(r, C - rem)].append((s, d, z))
                else:
                    next_shark_maps[(r, c - s)].append((s, d, z))

        shark_maps = next_shark_maps
        # 상어 정리
        for loc, sharks in shark_maps.items():
            if len(sharks) > 1:     # 제일 큰 상어가 나머지를 잡아먹는다
                lst_sharks = list(sharks)
                lst_sharks.sort(key=lambda x: x[2], reverse=True)
                king = lst_sharks[0]
                shark_maps[loc] = deque([king])

    print(sum(picked))


solution()
