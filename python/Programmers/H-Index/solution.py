def solution(citations):
    answer = 0
    sorted_citations = sorted(citations, reverse=True)
    for h in range(sorted_citations[0], 0, -1):
        for idx, num_citation in enumerate(sorted_citations):
            if num_citation >= h and (idx + 1) >= h:
                answer = max(answer, h)
        
    return answer