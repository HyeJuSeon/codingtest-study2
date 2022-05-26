from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(places):
    ans = []
    for p in places:
        seat = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    seat.append((i, j))
        flag = 1
        for s in seat:
            if not bfs(p, s):
                flag = 0
                break
        if flag:
            ans.append(1)
        else:
            ans.append(0)
    return ans

def bfs(p, s):
    a, b = s
    q = deque()
    q.append((a, b, 0))
    visit = [[0] * 5 for _ in range(5)]
    visit[a][b] = 1
    while q:
        x, y, dist = q.popleft()
        if dist > 2:
            break
        for i in range(4):
            nx, ny, ndist = x + dx[i], y + dy[i], dist + 1
            if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny]:
                if p[nx][ny] == 'O':
                    q.append((nx, ny, ndist))
                    visit[nx][ny] = 1
                elif p[nx][ny] == 'P' and dist < 2:
                    return 0
    return 1

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))