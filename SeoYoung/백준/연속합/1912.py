n=int(input())
dp=list(map(int,input().split()))

total_sum=dp[0]

for i in range(1,n):
    dp[i]=max(dp[i],dp[i-1]+dp[i])
    total_sum=max(total_sum,dp[i])

print(total_sum)
