## 풀이

동적계획법으로 풀어주었습니다.

cache는 그 위치의 숫자를 선택했을때 가질 수 있는 최대값입니다. 이 전의 값들 중(j-1) 같은 열의 위치를 제외하고 나머지 중에 가장 큰 값에 그 위치의 숫자를 더한 값을 저장해주었습니다.

## 코드

```python
def solution(land):
    n = len(land)
    cache = [[0 for _ in range(4)] for _ in range(n)]
    cache[0] = land[0][:]

    for j in range(1, n):
        for k in range(4):
            cache[j][k] = max(cache[j-1][:k] + cache[j-1][k+1:]) + land[j][k]

    return max(cache[n-1])
```
