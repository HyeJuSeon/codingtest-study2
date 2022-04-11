## 풀이

## 코드

```import sys

N = int(sys.stdin.readline())
graph = []

# 플로이드 와샬 알고리즘은 모든 정점에 대한 경로를 계산하는 알고리즘이다.
# 플로이드 와샬 알고리즘을 사용하여 어느 한 곳에 들려 다른 곳으로 가는 길이 존재한다면 그 값을 체킹해준다.
# 그리고 그 그래프를 출력하면 된다.

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for row in graph:
    out = " ".join(list(map(str,row)))
    print(out)


#삽질
'''
n = int(sys.stdin.readline())
graph = {}
#그래프 만들기
for key in range(1,n+1):
    line = list(map(int,sys.stdin.readline().strip().split()))
    value = []
    for idx, val in enumerate(line):
        if val:
            value.append(idx+1)
    graph[key] = value
print(graph)
result = []
def check(keys,graph):
    passed = []
    for key in keys:
        if len(graph[key]) != 0:
            passed += graph[key]
            check(i,graph)
    return passed
for i in range(1,n+1):
    node = [i]
    result.append(check(node,graph))
'''
```





