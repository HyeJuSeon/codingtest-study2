import sys
from math import inf

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    d = [[0] * K for _ in range(K)]
    for n in range(1, K):
        for i in range(K - n): # 오른쪽만
            j = i + n
            d[i][j] = inf
            s = sum(a[i:j + 1]) # i~j 누적
            for m in range(i, j):
                d[i][j] = min(d[i][j], d[i][m] + d[m + 1][j] + s)
    print(d[0][K - 1])