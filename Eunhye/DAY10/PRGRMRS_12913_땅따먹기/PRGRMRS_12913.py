def solution(land):
    n = len(land)
    cache = [[0 for _ in range(4)] for _ in range(n)]
    cache[0] = land[0][:]
    
    for j in range(1, n):
        for k in range(4):
            cache[j][k] = max(cache[j-1][:k] + cache[j-1][k+1:]) + land[j][k]

    return max(cache[n-1])