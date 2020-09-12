def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        bin_string = bin(a | b)[2:]
        if len(bin_string) < n:
            bin_string = ' ' * (n - len(bin_string)) + bin_string
        answer.append(bin_string)

    answer = list(map(lambda string: string.replace('0', ' '), answer))
    answer = list(map(lambda string: string.replace('1', '#'), answer))

    return answer
