## 풀이

## 코드

```
N = int(input())
T, P = [],[]
dp = [0] * (N+1)

for _ in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)

#뒤에서부터 접근해야한다
#Ti + 일자 > N+1 이면 dp[i]는 지나온 일자의 최대 이익인 dp[i+1]로 변경
#아닌 경우는 dp[i+1]과 현재 기준 날짜의 금액과 지나온 날짜의 최대 이익을 합산한 값을 비교
#최대값으로 변경
for i in range(N-1, -1, -1):
    if T[i] + i > N :
        dp[i] = dp[i+1]
    else:
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])

print(dp[0])
```
