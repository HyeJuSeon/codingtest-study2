'''백준 - 퇴사

- dp를 이용해서 각 위치에서 벌 수 있는 최대 금액을 기록
- dp의 max값을 반환하면 될듯..?

'''


n = int(input())

schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1): # 역방향으로 해당일에서 벌 수 있는 최대금액을 dp에 기록하며 인덱스 0까지 이동
    day, pay = schedule[i]
    if i + day > n: # 퇴사 전 해결하지 못하는 일인 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(pay + dp[i + day], dp[i+1]) # 새로 구한 수익과 기존 수익 중 큰 값 기록

print(dp[0])