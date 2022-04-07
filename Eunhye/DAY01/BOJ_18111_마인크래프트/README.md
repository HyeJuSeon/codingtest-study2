## 풀이

## 코드

```python
N, M, B = map(int, input().split())

field = []
for _ in range(N):
  field.extend(list(map(int, input().split())))

field.sort(reverse=True)

total = sum(field)
result = []
for height in range(field[0], -1, -1):
  idx = 0
  time = 0
  flag = 0
  blocks = B
  while idx < len(field) and height <= field[idx]:
    time += 2*(field[idx]-height)
    blocks += field[idx]-height
    idx += 1
    if result and time > result[0]:
      flag=1
      break

  while idx < len(field) and height > field[idx]:
    if blocks < height-field[idx]:
      flag = 1
      break
    time += height-field[idx]
    blocks -= height-field[idx]
    idx += 1
    if result and time > result[0]:
      flag=1
      break

  if not flag:
    result = [time, height] if not result or (result and time < result[0]) else result

print(*result, sep=" ")
```
