## 풀이

그리디로 풀어주었습니다.

지원자를 서류 순위로 정렬해준 뒤 가장 높은 서류 순위의 사람의 인터뷰 순위를 저장해준 뒤, 더 높은 순위를 가진 사람이 있다면 result를 누적해주었습니다.

## 코드

```python
T = int(input())
for _ in range(T):
  N = int(input())
  result = 1
  applicants = [ tuple(map(int, input().split())) for _ in range(N) ]
  applicants.sort()
  min_interview = applicants[0][1]
  for i in range(1, N):
    _, B_interview = applicants[i]
    if min_interview > B_interview:
      result += 1
      min_interview = B_interview

  print(result)
```
