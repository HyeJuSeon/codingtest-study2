## 백준 18111 마인크래프트

### 알고리즘

```txt
 ✅ 구현
 ✅ 완전탐색
```

### 코드 구현

사용 언어 : **파이썬**

```python
#pypy3으로 해결
import sys
read=sys.stdin.readline

N,M,B=map(int,read().split())
graph=[list(map(int, read().split())) for _ in range(N)]
# 그래프에서 가장 낮은 지점과 높은 지점을 각각 저장한 min_graph, max_graph
min_graph=min(map(min,graph))
max_graph=max(map(max,graph))
# 땅을 고르는 데 걸리는 최소 시간 min_time, 높이 height
min_time=10**8
height=-1

# 처음에는 블록의 개수(B)가 음수가 되면 while문 빠져나가고 height를 감소시키면서 실험
# => 예외 처리가 안됨 (전체적으로 탐색이 되기 전에 while문 빠져나가서)
# 필요하거나 빼야하는 블록개수를 모두 센 후에 한꺼번에 계산하는 방식으로 변환
for h in range(min_graph, max_graph+1):
    build=0
    remove=0

    for g in graph:
        for i in g:
            if i<h:
                build+=(h-i)

            elif i>h:
                remove+=(i-h)

    # 만약에 현재 높이로 땅을 골랐을 때 블록이 모자라지 않는다면
    if build<=remove+B:
        time=2*remove+build
        # 현재까지 저장된 최소 시간보다 현재 시간이 작다면 min_time, height 초기화
        if time<=min_time:
            min_time=time
            height=h

print(min_time, height)
```
