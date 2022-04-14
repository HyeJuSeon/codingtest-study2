import heapq
def solution(jobs):
    ans, end, i = 0, 0, 0
    start = -1
    hq = []
    while len(jobs) > i:
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(hq, (job[1], job[0]))
        if len(hq) > 0:
            now = heapq.heappop(hq)
            start = end
            end += now[0]
            ans += end - now[1]
            i += 1
        else:
            end += 1
    ans = ans // len(jobs)
    return ans

# print(solution([[0, 3], [1, 9], [2, 6]]))