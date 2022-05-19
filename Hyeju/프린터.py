from collections import deque

def solution(priorities, location):
    q = deque([(p, l) for l, p in enumerate(priorities)])
    ans = 0
    while q:
        maxq = max(q)[0]
        tmp = q.popleft()
        if tmp[0] == maxq:
            ans += 1
            if tmp[1] == location:
                return ans
        else:
            q.append(tmp)

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))