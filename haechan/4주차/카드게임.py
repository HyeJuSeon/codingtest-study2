'''백준 - 카드게임

- 선택지 : 가장 왼쪽 or 가장 오른쪽 둘 중 전략적 선택
- 잘못 가져갈 경우 상대가 큰 값을 가져가게 도와줄 수 있다
'''

import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input().strip())

    cards = list(map(int, input().split()))
    dp = [[0 for _ in range(N)] for _ in range(N)] 
    turn = 1 if N % 2 == 1 else -1 # True일 때 근우차례 
    
    for size in range(N):
        for i in range(N - size): 
            if size == 0: 
                dp[i][i+size] = cards[i] if turn == 1 else 0 
            elif turn == 1: #근우차례 
                dp[i][i+size] = max(dp[i+1][i+size] + cards[i], dp[i][i+size-1] + cards[i+size]) 
            elif turn == -1: #명우차례 
                dp[i][i+size] = min(dp[i+1][i+size], dp[i][i+size-1]) 
            
        turn *= -1
            
    print(dp[0][N-1])