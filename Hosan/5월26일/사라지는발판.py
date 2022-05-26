import sys
sys.setrecursionlimit(10**6)

visited = [[0] * 5 for _ in range(5)]
field = [[0] * 5 for _ in range(5)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = 0, 0

# 짝수 -> 패배, 홀수 -> 승리
def back(curx, cury, opx, opy):
    global visited, field
    if visited[curx][cury] == 1:
        return 0
    result = 0
    for i in range(4):
        nx = curx + dx[i]
        ny = cury + dy[i]
        #백트래킹 실행
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or field[nx][ny] == 0:
            continue
        visited[curx][cury] = 1
        val = back(opx, opy, nx, ny) + 1
        visited[curx][cury] = 0

        #결과값 정리
        # 패배 -> 승리 = 갱신
        if result % 2 == 0 and val % 2 == 1:
            result = val
        # 승리 -> 승리 = min 승리
        elif result % 2 == 1 and val % 2 == 1:
            result = min(result, val)
        # 패배 -> 패배 = max 패배
        elif result % 2 == 0 and val % 2 == 0:
            result = max(result, val)
    return result

def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            field[i][j] = board[i][j]
    return back(aloc[0], aloc[1], bloc[0], bloc[1])