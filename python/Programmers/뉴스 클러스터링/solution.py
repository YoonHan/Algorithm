def solution(str1, str2):
    answer = 0
    # 전처리
    str1 = str1.lower()
    str2 = str2.lower()

    # 다중 집합의 원소 만들기
    setA = []
    setB = []
    for idx in range(len(str1) - 1):
        if str1[idx: idx + 2].isalpha():
            setA.append(str1[idx: idx + 2])
    for idx in range(len(str2) - 1):
        if str2[idx: idx + 2].isalpha():
            setB.append(str2[idx: idx + 2])

    # 예외 처리
    if len(setA) == 0 and len(setB) == 0:
        return 65536
    elif len(setA) == 0 or len(setB) == 0:
        return 0

    # 자카드 유사도 구하기
    intersect = []
    union = []
    for elemA in setA:  # calculate intersection
        if elemA in setB:
            intersect.append(elemA)
            setB.remove(elemA)
        union.append(elemA)
    union.extend(setB)
    answer = int(len(intersect) / len(union) * 65536)

    return answer
