def solution(triangle):
    #점화식 만들기
    dp = [[0]*i for i in range(1,len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            # 왼쪽 숫자
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j]) 
            # 가운데, 오른쪽 숫자
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1]) 
            
    return max(dp[-1])
