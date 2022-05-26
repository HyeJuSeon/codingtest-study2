dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])

    def dfs(board, loc1, loc2, d):
        x1, y1 = loc1
        x2, y2 = loc2
        win = 0
        d_max = d
        d_min = 25
        if board[x1][y1]:
            for i in range(4):
                nx, ny = x1 + dx[i], y1 + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or not board[nx][ny]:
                    continue
                board[x1][y1] = 0
                nwin, nd = dfs(board, [x2, y2], [nx, ny], d + 1) # 상대 턴
                win = 1 if win or not nwin else 0
                if nwin:
                    d_max = max(d_max, nd)
                else:
                    d_min = min(d_min, nd)
                board[x1][y1] = 1
        return win, d_min if win else d_max

    _, ans = dfs(board, aloc, bloc, 0)
    return ans

# print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
# print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
# print(solution([[1]], [0, 0], [0, 0]))