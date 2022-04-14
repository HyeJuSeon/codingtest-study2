## 풀이

그리디로 풀어주었습니다.
덧셈을 먼저 해준 뒤, 뺄셈을 해주는 방법입니다.

## 코드

```python
import math

S = input()

opers, nums, = [], []
start, plus = 0, 0

result = math.inf

for i in range(len(S)):
  if S[i] == "+" or S[i] == "-":
    nums.append(int(S[start:i]))
    opers.append(S[i])
    start = i+1
    plus += 1 if S[i] == "+" else 0
nums.append(int(S[start:]))

if plus != len(opers):
  idx = 0
  while opers:
    # print(nums, opers)
    if opers[idx] == "+":
      nums[idx] += nums[idx+1]
      nums.pop(idx+1)
      opers.pop(idx)
      plus -= 1
      idx = 0
    elif opers[idx] == "-" and not plus:
      nums[idx] -= nums[idx+1]
      nums.pop(idx+1)
      opers.pop(idx)
      idx = 0
    else:
      idx += 1
  result = nums[0]
else:
  result = sum(nums)

print(result)
```
