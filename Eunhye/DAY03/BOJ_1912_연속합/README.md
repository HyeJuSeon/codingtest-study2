## 풀이

동적계획법으로 풀어주었습니다.

이전까지의 값을 더해주는 것과 더하지 않은 현재의 값을 비교해 더 큰 값을 저장해주었습니다.

## 코드

```python
N = int(input())
arr = list(map(int, input().split()))
cache = [0 for _ in range(N)]
cache[0] = arr[0]
for i in range(1, N):
    cache[i] = max(cache[i-1]+arr[i], arr[i])
print(max(cache))
```
