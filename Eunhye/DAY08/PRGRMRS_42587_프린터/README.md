## 풀이

deque를 이용하여 풀어주었습니다.

priorities의 index를 저장하는 idx를 deque로 만들어줍니다.

max_prior에는 가장 높은 우선순위의 값을 저장해줍니다.

가장 높은 우선순위가 아니라면 popleft해주고 바로 append해주어 뒤로 보내줍니다. 가장 높은 우선순위라면 popleft해주고 answer를 1 증가시켜줍니다.

방금 pop해준 값을 poped에 저장해주고, location과 일치하다면 바로 answer를 return해줍니다. 일치하지 않다면 max_prior를 pop해준 값을 제외한 priorities에서 업데이트해줍니다.

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
