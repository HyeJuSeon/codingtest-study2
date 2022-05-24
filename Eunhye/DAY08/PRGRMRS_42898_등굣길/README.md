## 풀이

## 코드

```python
def solution(m, n, puddles):
    # 모든 지역 1로 초기화
    graph = [[1 for _ in range(m)] for _ in range(n)]

    # 침수 지역 표시
    for px, py in puddles:
        graph[py-1][px-1] = 0

    # 아래로만 가능 경우 초기화
    # 침수 지역을 만나게 되면 더이상 아래로 갈 수 없다.
    for i in range(1, n):
        if graph[i-1][0] == 0:
            graph[i][0] = 0

    # 오른쪽으로만 가능 경우 초기화
    # 침수 지역을 만나게 되면 더이상 오른쪽으로 갈 수 없다.
    for j in range(1, m):
        if graph[0][j-1] == 0:
            graph[0][j] = 0

    # 각각 왼쪽, 위의 방향에서 오는 경우만 해당 좌표에 도달할 수 있다.
    for y in range(1, n):
        for x in range(1, m):
            if graph[y][x] == 0:
                continue
            graph[y][x] = (graph[y-1][x] + graph[y][x-1]) % 1000000007

    return graph[n-1][m-1]
```
