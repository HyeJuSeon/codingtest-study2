from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    jobs.sort()
    ready = []
    idx = 0
    time = 0
    while idx < len(jobs) or ready:
        while idx < len(jobs) and jobs[idx][0] <= time:
            heappush(ready, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if ready:
            duration, req_time = heappop(ready)
            answer += (time - req_time) + duration
            time += duration
        else: time += 1
    return answer // len(jobs)