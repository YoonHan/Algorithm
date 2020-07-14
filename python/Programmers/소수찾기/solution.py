from itertools import permutations


def prime_check(number):
    if number == 0 or number == 1:
        return False
    is_prime = True
    i = 2
    while i**2 <= number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    return is_prime


def solution(numbers):
    answer = 0

    numbers = list(numbers)
    candidates = []
    for digit in range(1, len(numbers) + 1):
        for case in permutations(numbers, digit):
            candidates.append(int(''.join(case)))

    candidates = set(candidates)
    for candidate in candidates:
        if prime_check(candidate):
            answer += 1

    return answer
