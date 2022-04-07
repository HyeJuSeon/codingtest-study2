import sys
from math import inf
N, M, B = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
h = 0
ans = inf
for k in range(257):
    to_inv_cnt = 0
    from_inv_cnt = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] < k:
                from_inv_cnt += k - Map[i][j]
            else:
                to_inv_cnt += Map[i][j] - k
    inven = to_inv_cnt + B
    if inven < from_inv_cnt:
        continue
    t = 2 * to_inv_cnt + from_inv_cnt
    if t <= ans:
        ans = t
        h = k
print(ans,  h)