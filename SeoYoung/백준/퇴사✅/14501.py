n=int(input())
works=[list(map(int,input().split())) for _ in range(n)]
dp=[0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    #n일이 넘어가면 
    if i+works[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], works[i][1]+dp[i+works[i][0]])

print(dp[0])