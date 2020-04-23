from sys import stdin
input = stdin.readline

N = int(input())
works = [[*map(int, input().split())] for _ in range(N)]
max_rewards = [0] * N

# i 일차에서 얻을 수 있는 최대 보상 :
#     a. i일차 보상 + (i + day)일차 최대 보상
#     b. i + 1 일차에서 얻을 수 있는 최대 보상
# 둘 중에 큰 거 고르기


def solution():
    for i in range(N - 1, -1, -1):
        day = works[i][0]
        reward = works[i][1]
        if i == N - 1:     # 마지막 일차에선 그 일을 하거나 안하거나 둘 중 하나
            if day == 1:
                max_rewards[i] = reward
                continue
            else:
                continue

        if i + (day - 1) >= N:
            max_rewards[i] = max_rewards[i + 1]   # 근무 기간 벗어난 경우
        elif i + (day - 1) == N - 1:  # 정확히 마지막 날에 끝나는 경우
            max_rewards[i] = max(reward, max_rewards[i + 1])

        elif i + day <= N - 1:  # i 일째 일을 끝내고 i + day 일째 일을 할 수 있을 경우
            max_rewards[i] = max(
                reward + max_rewards[i + day], max_rewards[i + 1])


solution()
print(max_rewards[0])
