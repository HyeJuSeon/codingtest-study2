## 풀이

## 코드

```
#시간초과 
import sys
from collections import Counter

N, M, B = map(int,sys.stdin.readline().strip().split())

flatten = []

for i in range(N):
    flatten += (list(map(int,sys.stdin.readline().strip().split())))

h_lst = set(flatten)

result_h = 0
time_list = []
temp = True

for h in h_lst:
    inven = B
    time = 0

    for spot,count in Counter(flatten).items():
        if spot == h:
            pass
        elif spot < h:
            block = (h-spot)*count
            if inven >= block:
                time += block
                inven -= block
            else:
                continue

        elif spot > h:
            block = (spot-h)*count
            time += block * 2
            inven += block
    
    time_list.append(time)
    min_time = min(time_list)

    if min_time >= time:
        result_h = h
        min_time = time
    else:
        continue

sys.stdout.write(min_time, result_h)

```







