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