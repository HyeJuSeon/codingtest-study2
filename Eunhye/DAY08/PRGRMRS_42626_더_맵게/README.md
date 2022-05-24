## 풀이

## 코드

```python
from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        lowest = heappop(scoville)
        second = heappop(scoville)
        answer += 1
        heappush(scoville, lowest+second*2)
    return answer if scoville[0] >= K else -1
```
