# permutaion 직접 구현


def permutation(lst):
    permu = []
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    # if more than 1 characters
    for i in range(len(lst)):
        head = lst[i]
        rem_lst = lst[:i] + lst[i + 1:]
        for p in permutation(rem_lst):
            permu.append([head] + p)
    return permu


a = [1, 2, 3, 4]
for line in (permutation(a)):
    print(line)
