import heapq

v,e = map(int,input().split())
k = int(input()) - 1

# 최단 경로값을 구해서 채워줄 리스트
# 경로를 지나며 누적된 가중치의 최소값이 원소로 들어갈 예정
dist = [float('inf')] * v
dist[k] = 0

# 그래프 정리
linked = [[] for i in range(v)]
for i in range(e):
    a,b,w = map(int,input().split())
    linked[a-1].append((b-1,w))

# print(linked)
heap = []
heapq.heappush(heap, (0, k))


while(heap):
    cur_dist, cur_node = heapq.heappop(heap)
    # 힙에서 하나씩 뽑으면서 cur_dist, cur_node 업데이트
    if dist[cur_node] < cur_dist:
        continue

    # print : linked[cur_node] => [(1,2),(2,3)]
    for to_node, to_dist in linked[cur_node]:
        sum_dist = cur_dist + to_dist
        # 최단경로 업데이트
        # 최단경로 정보를 힙에 푸시
        if sum_dist < dist[to_node]:
            dist[to_node] = sum_dist
            heapq.heappush(heap,(sum_dist,to_node))


for i in dist:
    print(i if i != float('inf') else "INF")





















'''
재귀 완전탐색 Recursive 에러뜸

v,e = map(int,input().split())
k = int(input())

info = [list(map(int,input().split())) for i in range(e)]
start_node = [n[0] for n in info]


def solution(node,target,count):
    global count_lst
    if node not in start_node:
        count_lst.append(0)
        return

    for i in info:
        if node == i[0] and target == i[1]:
            count += i[2]
            count_lst.append(count)
            return

        elif node == i[0]:
            count += i[2]
            solution(i[1], target, count)
            count -= i[2]
    return

for i in range(1,v+1):
    if i == k:
        print(0)
        continue
    count_lst = []
    solution(k, i, 0)
    min_value = min(count_lst)
    if min_value == 0:
        print('INF')
    else:
        print(min_value)
'''