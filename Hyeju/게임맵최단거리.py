dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visit = [[0 for _ in range(col)] for _ in range(row)]
    visit[0][0] = 1

    q = [(0, 0)]
    while q:
        a, b = q.pop(0)
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if -1 < x < row and -1 < y < col:
                if maps[x][y]:
                    if not visit[x][y]:
                        visit[x][y] = visit[a][b] + 1
                        q.append((x, y))
    ans = visit[-1][-1]
    if ans:
        return ans
    return -1

# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
