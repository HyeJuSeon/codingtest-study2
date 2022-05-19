# x가 3으로 나누어 떨어지면 3으로 나눈다
# x가 2로 나누어 떨어지면 2로 나눈다
# 1을 뺀다
INF=10**6
N=int(input())
dp=[INF] * (N+1)
dp[1]=0
route=[[] for _ in range(N+1)]

for i in range(1,N):
    if dp[i+1]>dp[i]+1:
        dp[i+1]=dp[i]+1
        route[i+1]=route[i]+[i+1]
    if i*2<=N and dp[i*2]>dp[i]+1:
        dp[i*2]=dp[i]+1
        route[i*2]=route[i]+[i*2]
    if i*3<=N and dp[i*3]>dp[i]+1:
        dp[i*3]=dp[i]+1
        route[i*3]=route[i]+[i*3]

print(dp[N])
for i in route[N][::-1]:
    print(i, end=' ')
print(1)
