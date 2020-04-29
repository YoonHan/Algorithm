from collections import defaultdict, deque

r, c, k = list(map(int, input().split()))
array = [[*map(int, input().split())] for _ in range(3)]


def solution():
    global r, c, k, array   # r, c 에서 1 빼줘야 함.
    lapsed = 0

    while True:
        # 정답 체크
        rows = len(array)
        cols = len(array[0])
        if 0 <= r - 1 < rows and 0 <= c - 1 < cols and array[r - 1][c - 1] == k:
            break
        if lapsed > 100:
            lapsed = -1
            break

        next_array = []
        # R 연산
        if len(array) >= len(array[0]):
            max_len = -1
            for row in array:
                count = defaultdict(int)
                for item in row:
                    if item != 0:
                        count[item] += 1
                new_row = []
                count = list(count.items())
                count.sort(key=lambda x: (x[1], x[0]))
                for key, value in count:
                    new_row.append(key)
                    new_row.append(value)
                next_array.append(new_row)
                if max_len < len(new_row):
                    max_len = len(new_row)
            # 0 채우기
            for row in next_array:
                diff_count = max_len - len(row)
                if diff_count > 0:
                    for _ in range(diff_count):
                        row.append(0)
        # C 연산
        elif len(array) < len(array[0]):
            max_len = -1
            for col in zip(*array):
                count = defaultdict(int)
                for item in col:
                    if item != 0:
                        count[item] += 1
                new_col = []
                count = list(count.items())
                count.sort(key=lambda x: (x[1], x[0]))
                for key, value in count:
                    new_col.append(key)
                    new_col.append(value)
                next_array.append(new_col)
                if max_len < len(new_col):
                    max_len = len(new_col)
            # 0 채우기
            for row in next_array:
                diff_count = max_len - len(row)
                if diff_count > 0:
                    for _ in range(diff_count):
                        row.append(0)
            # transpose
            next_array_transposed = []
            for col in zip(*next_array):
                next_array_transposed.append(list(col))
            next_array = next_array_transposed

        array = next_array
        # 배열 크기 체크 (100 초과인지)
        diff = len(array[0]) - 100
        if diff > 0:
            for row in enumerate(array):
                for _ in range(diff):
                    row.pop()
        # 시간 늘리기
        lapsed += 1
    print(lapsed)


solution()
