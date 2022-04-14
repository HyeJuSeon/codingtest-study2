## 풀이

우선 jobs를 요청시간이 가장 빠른 순서로 오름차순 정렬해주었습니다.
아래와 같은 조건 아래에 돌아주었습니다.

- idx가 jobs의 길이보다 작다 = 아직 요청하지 않은 작업이 있다
- ready가 비어있지 않다 = 대기 중인 처리하지 않은 작업이 있다

현재 time이 요청시간과 같거나 크다면 heappush를 이용해 ready에 넣어주는데 원래의 순서와 반대로 이번에는 작업의 소요시간을 앞부분에 넣어주어 ready가 작업 소요시간이 작은 순으로 정렬되게끔 해줍니다.

ready가 비어있지 않다면 heappop을 이용해 대기 중인 작업들 중 가장 소요시간이 작은 작업을 꺼내주고, 요청하고 대기한 시간(time - req_time)과 소요시간(duration)을 더해준 값을 answer에 누적해주고 time을 duration만큼 누적해줍니다.

ready가 비어있다면 time을 늘려줍니다.

## 코드

```python
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
```
