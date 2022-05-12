import sys
input = sys.stdin.readline
inf = sys.maxsize

N = int(input())

for i in range(N) :
    size = int(input())
    data = list(map(int, input().split()))
    dp = [[0] * size for _ in range(size)]
    Sum = [0]
    for d in data :
        Sum.append(Sum[-1] + d)
    for d in range(1,size) :
        for i in range(size - d) :
            j = d + i #대각선 인덱스
            dp[i][j] = inf
            for k in range(i, j) :
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + Sum[j+1] - Sum[i])
    print(dp)
    print(dp[0][size-1])

