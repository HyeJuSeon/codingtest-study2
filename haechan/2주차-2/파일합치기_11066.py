'''
[파일합치기]

dp[1][2] => 1 ~ 2 최소 합
dp[1][3] => 1 ~ 3 최소 합
'''

import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int,input().split())) # 순서를 맞춰주기 위해 0번째 인덱스에 채우기용 값 추가
    dp = [[0]*(K+1) for _ in range(K+1)]
    
    for i in range(2, K+1): # 파일은 최소 2개부터 k+1개까지 합칠 수 있다
        for j in range(1, K+1-(i-1)): # 5-(i-1) = 4,3,2,1

            # dp[1][3]이라면 1 ~ 3까지의 발생할 수 있는 합 중 최소값 + 남은 값의 합
            dp[j][j+i-1] = min(dp[j][j+n] + dp[j+n+1][j+i-1] for n in range(i-1)) + sum(files[j:j+i])
            
    print(dp[1][K])