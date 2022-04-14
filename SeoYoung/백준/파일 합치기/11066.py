import math

tc=int(input())

for _ in range(tc):
    n=int(input())
    files=[0]+list(map(int,input().split()))
    s=[0 for _ in range(n+1)]
    # s[i] 는 1번부터 i까지의 누적합
    for i in range(1,n+1):
        s[i]=s[i-1]+files[i]
    

    dp=[[0 for _ in range(n+1)] for _ in range(n+1)]     
    # 부분 파일의 길이 i, 시작점 j
    # dp[i][k] + dp[k+1][j] + sum(A[i]~A[j])
    for i in range(2,n+1):
        for j in range(1, n+2-i):
            dp[i][j]=min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + s[j+i-1]-s[j-1]


    print(dp[1][n])    
    