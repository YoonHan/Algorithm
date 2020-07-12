def solution(arrangement):
    answer = 0

    stack = []
    prev = ''
    for letter in arrangement:
        if letter == '(':
            stack.append(letter)
        elif prev == '(' and letter == ')':
            stack.pop()
            answer += len(stack)
        elif prev == ')' and letter == ')':
            stack.pop()
            answer += 1
        prev = letter

    return answer
