import sys
from collections import Counter
#시간초과
N, M, B = map(int,sys.stdin.readline().strip().split())

flatten = []

for i in range(N):
    flatten += (list(map(int,sys.stdin.readline().strip().split())))

h_lst = range(min(flatten),max(flatten)+1)

result_h = 0
time_list = []
temp = True

for h in h_lst:
    inven = B
    time = 0

    #여기가 문제임
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

print(min_time, result_h)

