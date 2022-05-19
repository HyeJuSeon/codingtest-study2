from collections import deque

def solution(priorities, location):
    dq = deque([[v, i] for i, v in enumerate(priorities)])
    answer = 0
    while len(dq):
        item = dq.popleft()
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if location == item[1]:
                return answer