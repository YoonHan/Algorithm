import re


def solution(dartResult):
    answer = 0
    # define regular expression
    regex_num = re.compile('\d+')
    regex_ops = re.compile('[SDT][#*]?')
    # separate numbers from operations
    nums = list(map(int, regex_num.findall(dartResult)))
    ops = regex_ops.findall(dartResult)
    # calculate
    for idx, op in enumerate(ops):
        # doubling or tripling each number
        if op[0] == 'D':
            nums[idx] = nums[idx] ** 2
        elif op[0] == 'T':
            nums[idx] = nums[idx] ** 3
        # operation with special character
        if len(op) == 2 and op[1] == '#':
            nums[idx] *= -1
        elif len(op) == 2 and op[1] == '*':
            if idx >= 1:
                nums[idx - 1] *= 2
                nums[idx] *= 2
            else:
                nums[idx] *= 2
    # get answer
    answer = sum(nums)

    return answer
