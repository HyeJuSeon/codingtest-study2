n=int(input())
works=[list(map(int,input().split())) for _ in range(n)]
dp=[0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    # n일이 넘어가면 할 수 없는 일이므로 0저장
    if i+works[i][0]>n:
        dp[i]=dp[i+1]
    
    else:
        # max(i+1일부터 벌 수 있는 최대 금액, i일에 시작한 일의 금액 + 일이 끝난 시점부터 벌 수 있는 최대 금액)
        dp[i]=max(dp[i+1], works[i][1]+dp[i+works[i][0]])

print(dp[0])