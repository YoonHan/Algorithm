def solution(heights):
    answer = []
    for idx, selected in enumerate(heights):
        is_found = False
        for pos in range(idx - 1, -1, -1):
            if heights[pos] > selected: 
                answer.append(pos + 1)
                is_found = True
                break
        if not is_found:
            answer.append(0)
               
    return answer