# 땅 고르기 작업
# N * M의 집터를 고름 
# 집터 내의 땅의 높이를 일정하게 고르는 작업을 해야함
# 1. 좌표의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다 (2초)
# 2. 인벤토리에서 블록 하나를 꺼내어 좌표의 가장 위에 있는 블록 위에 넣는다 (1초)
# 최대한 빨리 땅 고르기 작업을 마쳐야 하고, 작업에 걸리는 최소 시간과 그 때의 땅의 높이
# 땅의 높이는 256 블록 초과 x 음수 x 
# 입력 N, M, B(인벤토리 블록 개수)
# 출력 최소 시간, 블록 높이
# 고르게 하는 게 관건 ! 평균 반올림

# 땅의 높이의 평균값을 구해서 시도해보려고 했던.. 일부 반례가 존재 - 실패
'''
from functools import reduce

N,M,B=map(int,input().split())
graph=[list(map(int, input().split())) for _ in range(N)]
height=round(reduce(lambda acc, cur: acc+sum(cur), graph, 0)/(N*M))
time=0
flag=False
blocks=B

while True:
    for g in graph:
        for i in g:
            # 블록을 쌓아야 할 때 (1초)
            if i<height: 
                blocks-=(height-i)
                if blocks<0:
                    flag=True
                    break
                time+=(height-i)
            # 블록 제거해야할 때 (2초)
            elif i>height:
                blocks+=(i-height)
                time+=2*(i-height)
        if flag==True:
            time=0
            height-=1
            blocks=B
            flag=False
            break
    else:
        break

print(time, end=' ')
print(height)
'''
import sys
read=sys.stdin.readline

N,M,B=map(int,read().split())
graph=[list(map(int, read().split())) for _ in range(N)]
min_graph=min(map(min,graph))
max_graph=max(map(max,graph))
min_time=10**8
height=-1

for h in range(min_graph, max_graph+1):
    build=0
    remove=0

    for g in graph:
        for i in g:
            if i<h:
                build+=(h-i)

            elif i>h:
                remove+=(i-h)

    if build<=remove+B:
        time=2*remove+build

        if time<=min_time:
            min_time=time
            height=h

print(min_time, end=' ')
print(height)