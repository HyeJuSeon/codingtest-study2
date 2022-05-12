from collections import deque
#bfs

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    graph = [[-1 for _ in range(col)] for _ in range(row)]
    visited = deque()
    visited.append([0,0])
    graph[0][0] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while visited:
        x, y = visited.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < row and nx >= 0 and ny < col and ny >= 0:
                if maps[nx][ny] == 1:
                    if graph[nx][ny] == -1:
                        graph[nx][ny] = graph[x][y] + 1
                        visited.append([nx, ny])
                        # print(*graph,sep='\n')
                        # print(visited)
    answer = graph[-1][-1]
    return answer



maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
solution(maps)
