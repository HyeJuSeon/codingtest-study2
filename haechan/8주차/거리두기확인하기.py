from collections import deque

def bfs(sx, sy, place):
    dx = [0, 0, -1, 1] # 좌, 우
    dy = [-1, 1, 0, 0] # 상, 하
    visited = [[0]*5 for _ in range(5)]
    dq = deque()
    dq.append((sx, sy))
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if sx == nx and sy == ny:
                continue
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                continue
            if visited[nx][ny] != 0: # 이미 방문한 경우
                continue
            if place[nx][ny] == 'X': # 칸막이인 경우
                continue
            if place[nx][ny] == 'P': # 처음 출발한 P로부터 가장 가까운 P를 만났을 때
                visited[nx][ny] += visited[x][y] + 1
                if visited[nx][ny] <= 2: # visited에 기록한 거리가 곧 두 좌표의 맨해튼 거리
                    return 0
            if place[nx][ny] == 'O':
                dq.append((nx, ny))
                visited[nx][ny] += visited[x][y] + 1 # visited에 이동한 거리를 합산기록한다.

    return 1

        
def solution(places):
    result = []
    for idx, place in enumerate(places):
        tmp = []
        for i, p1 in enumerate(place):
            for j, p2 in enumerate(p1):
                if p2 == 'P':
                    tmp.append(bfs(i, j, place))
        if 0 in tmp:
            result.append(0)
        else:
            result.append(1)
    
    return result