N = int(input())
scores = list(map(int, input().split()))


def solution():
    global N, scores
    max_score = max(scores)
    new_score = []
    for score in scores:
        new_score.append((score / max_score) * 100)
    print(sum(new_score) / len(new_score))


solution()
