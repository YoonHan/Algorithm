from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities * 5)

    # make cache as deque(queue)
    cache = deque([])
    # make all city names lowercase
    cities = [city.lower() for city in cities]
    # calculate execution time
    answer = 0
    for city in cities:
        if city in cache:  # cache hit
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:             # cache miss
            answer += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)

    return answer
