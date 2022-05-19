def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for col, row in puddles:
        dp[row][col] = -1
    dp[1][1] = 1
    def dyn(row, col):
        if row < 1 or col < 1 or dp[row][col] < 0:
           return 0
        if dp[row][col] > 0:
            return dp[row][col]
        dp[row][col] = dyn(row, col-1) + dyn(row-1, col)
        return dp[row][col]
    return dyn(n, m) % 1000000007