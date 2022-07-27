## 풀이

BFS로 풀어주었습니다.  

visited를 따로 만들어주지 않고 map의 값을 바꿔주었습니다. y와 x좌표를 tuple로 넣어주며 popleft를 해주면서 최단거리를 구해주었습니다.  

갈 수 있는 모든 거리에 벽이 없는지 확인(map의 값이 1인지 확인)해주며 벽이 없다면 해당 좌표에 현 위치의 map 값을 더해주면서 누적해주었습니다. map의 값이 1일 때만 더해주기 때문에 방문을 이미 했다면 더해주지 않기 때문에 마지막 좌표에는 최소거리가 저장되게 됩니다.

마지막에는 도착좌표의 map값이 여전히 1이라면 도달할 수 없는 것이므로 -1을, 그렇지 않다면 map값을 return 해줍니다.  

## 코드

```python
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = 0
    queue = deque([(0,0)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] += maps[y][x]
                queue.append((ny, nx))

    # print(*maps, sep="\n")
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]
```
