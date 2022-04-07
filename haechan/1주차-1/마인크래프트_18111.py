'''백준 18111번 - 마인크래프트

- max_h 부터 min_h까지 내려가면서 해당 높이로 맞췄을 때의 (최단 소요시간, 높이) 구하기
- 최단 소요시간이면서 최대 높이인 값을 구해야 한다 ==> 블록을 쌓는게 1초로 짧으니까 높은 걸 타겟으로 잡아서 먼저 수행
'''

import sys
from collections import Counter

input = sys.stdin.readline
row, col, block_cnt = map(int, input().split())
blocks = []

max_h, min_h = 0, 256
for _ in range(row):
    rows = list(map(int, input().split()))
    blocks.extend(rows)
    max_h, min_h = max(max_h, max(rows)), min(min_h, min(rows))


# 순서가 없으니까 Counter로 각 높이의 개수를 구해서 해당 높이를 한번에 처리하는 방식
# {44: 2, 29: 1, 51: 1, 54: 1, 22: 1, 32: 1, 62: 1, 25: 1, 38: 1, 16: 1, 2: 1}
counter = Counter(blocks)
result = []
for target_h in range(max_h, min_h-1, -1):
    inventory = block_cnt
    needed_block = 0
    spend_time = 0
    for block_h, block_num in counter.items():
        if block_h > target_h: # 타겟 높이보다 높은 경우 --> 블록 제거 2초
            action_cnt = block_h - target_h
            inventory += action_cnt * block_num
            spend_time += 2 * action_cnt * block_num
        elif block_h < target_h: # 타겟 높이보다 낮은 경우 --> 블록 쌓기 1초
            action_cnt = target_h - block_h
            needed_block += action_cnt * block_num
            spend_time += action_cnt * block_num 

    if inventory >= needed_block: # 인벤토리에 있는 블록 수가 필요한 블록 수보다 같거나 크다면 가능
        result.append((spend_time, target_h))
        
result.sort(key=lambda x: (x[0], -x[1])) # 최소 시간이면서 땅의 높이가 높은 순으로 정렬
print(result[0][0], result[0][1])