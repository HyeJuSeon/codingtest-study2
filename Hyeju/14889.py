import sys
from math import inf
from itertools import combinations

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
l = range(N)
combs = list(combinations(l, N // 2))

ans = inf
for comb in combs[:len(combs) // 2]:
    comb2 = [x for x in l if x not in comb]
    start = 0
    link = 0
    cases = list(combinations(comb, 2))
    for case in cases:
        i, j = case
        start += S[i][j] + S[j][i]
    cases = list(combinations(comb2, 2))
    for case in cases:
        i, j = case
        link += S[i][j] + S[j][i]
    ans = min(ans, abs(start - link))
print(ans)