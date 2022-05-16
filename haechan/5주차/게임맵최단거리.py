'''프로그래머스 - 게임 맵 최단거리

# 지나가야 하는 칸의 개수의 최솟값 => 최단거리니까 bfs
# 상대편 좌표인 n, m 을 감싸는 위치가 0이면 접근 못하는 거니까
  -1을 반환하려했으나 몇몇 케이스에서 실패 발생.. 그냥 없앰

'''

from collections import deque

# 최소 칸의 개수 리턴
def bfs(maps, n, m):
    dq = deque()
    dq.append((0, 0))
    mx = [0, 0, -1, 1]
    my = [-1, 1, 0, 0]
    
    while dq:
        x, y = dq.popleft()
        
        if x == n and y == m:
            break
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            
            if nx < 0 or ny < 0 or nx > n or ny > m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                dq.append((nx, ny))
            
    return maps[n][m]
        

def solution(maps):
    n, m = len(maps)-1, len(maps[0])-1 # 행 개수, 열 개수 (4, 4)
    result = bfs(maps, n, m)
    if result == 1:
        return -1
    return result