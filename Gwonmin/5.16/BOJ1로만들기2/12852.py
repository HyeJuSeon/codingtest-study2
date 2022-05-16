# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

#dp 풀이
N = int(input())
dp = [[0, []] for _ in range(N+1)]
dp[1][0] = 0
dp[1][1] = [1]
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    if i%2 == 0 and dp[i//2][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]
    if i%3 == 0 and dp[i//3][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
print(dp[-1][0])
print(*dp[-1][1][::-1])

#bfs 풀이
from collections import deque

def bfs(node, dp):
    q = deque()
    q.append((node, dp))
    while q:
        node, dp = q.popleft()
        for n in [node+1, node*2, node*3]:
            if n <= N and check[n] == 0:
                if n == N:
                    return check[node]+1, dp+[n]
                q.append((n, dp+[n]))
                check[n] = check[node]+1

N = int(input())
if N == 1:
    print(0)
    print(1)
else:
    check = [0]*(N+1)
    cnt, dp = bfs(1, [1])
    print(cnt)
    print(*dp[::-1])