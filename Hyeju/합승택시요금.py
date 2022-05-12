from math import inf

def solution(n, s, a, b, fares):
    N = n + 1
    g = [[inf for _ in range(N)] for _ in range(N)]
    for i, j, c in fares:
        g[i][j] = c
        g[j][i] = c

    for k in range(1, N):
        for i in range(1, N):
            for j in range(1, N):
                if i == j:
                    g[i][j] = 0
                else:
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    ans = inf
    for i in range(1, N):
        ans = min(ans, g[s][i] + g[i][a] + g[i][b])
    return ans

# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))