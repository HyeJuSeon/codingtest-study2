from collections import Counter

def solution(gems):
    answer = []
    cnt_gems = Counter(gems)
    start, end = 0, len(gems)
    for e in range(len(gems)-1, -1, -1):
        if cnt_gems[gems[e]] == 1:
            end = e
            break
        cnt_gems[gems[e]] -= 1
    for e in range(end, len(gems)):
        while start < e:
            if start < len(gems) and cnt_gems[gems[start]] == 1:
                break
            cnt_gems[gems[start]] -= 1
            start += 1
        answer.append([start+1, e+1])
        if e+1 < len(gems):
            cnt_gems[gems[e+1]] += 1

    return sorted(answer, key=lambda x:(x[1]-x[0], x[0]))[0]