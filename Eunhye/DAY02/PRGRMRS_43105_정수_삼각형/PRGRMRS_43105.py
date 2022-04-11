def solution(triangle):
    N = len(triangle)
    cache = [[0 for _ in range(n+1)] for n in range(N)]
    cache[0][0] = triangle[0][0]
    if N > 1:
        cache[1][0] = cache[0][0] + triangle[1][0]
        cache[1][1] = cache[0][0] + triangle[1][1]
        for i in range(2, N):
            cache[i][0] = cache[i-1][0] + triangle[i][0]
            cache[i][i] = cache[i-1][i-1] + triangle[i][i]
            for j in range(1, i):
                cache[i][j] = max(cache[i-1][j-1], cache[i-1][j]) + triangle[i][j]
    return max(cache[N-1])