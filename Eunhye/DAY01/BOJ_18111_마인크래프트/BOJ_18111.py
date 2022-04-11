N, M, B = map(int, input().split())

field = []
for _ in range(N):
  field.extend(list(map(int, input().split())))

field.sort(reverse=True)
cumul = [0 for _ in range(len(field))]
cumul[0] = field[0]
for idx in range(1, len(field)):
  cumul[idx] = cumul[idx-1]+field[idx]
result = []
for height in range(field[0], -1, -1):
  idx = 0
  time = 0
  blocks = B
  while idx < len(field)-1 and field[idx] > height:
    idx += 1
  print(height, idx, field[idx])
    # if height <= field[idx]:
    #   time += 2*(field[idx]-height)
    #   blocks += field[idx]-height
    #   idx += 1
    #   if result and time > result[0]:
    #     break
    # else:
    #   if blocks < height-field[idx]:
    #     break
    #   time += height-field[idx]
    #   blocks -= height-field[idx]
    #   idx += 1
    #   if result and time > result[0]:
    #     break
#   else:
#     result = [time, height] if not result or (result and time < result[0]) else result

# print(*result, sep=" ")