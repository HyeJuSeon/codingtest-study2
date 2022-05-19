## 풀이

## 코드

```python
from collections import deque

def solution(priorities, location):
    idx = deque(range(len(priorities)))
    answer = 0
    max_prior = max(priorities)

    while True:
        if priorities[idx[0]] != max_prior:
            idx.append(idx.popleft())
            continue

        poped = idx.popleft()
        answer += 1

        if poped == location:
            return answer
        max_prior = max([priorities[i] for i in idx])
```
