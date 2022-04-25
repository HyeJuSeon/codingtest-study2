'''
[연구소]
1. 주어진 연구소에서 3개의 벽(1)을 선택
2. 벽이 선택된 연구소에 바이러스(2)를 퍼트린다
3. 바이러스가 퍼지지 않은 안전지역(0)의 개수 세기
'''

from collections import deque
import sys, copy


def bfs(graph, n, m, virus_list):
    global max_zero
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    dq = deque()
    
    for virus in virus_list:
        dq.append(virus) # 바이러스를 시작점으로 해서 퍼트릴 수 있도록 큐에 넣어준다
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dq.append((nx, ny))
    
    zero_cnt = 0     
    for i in range(n):
        zero_cnt += graph[i].count(0)
        
    max_zero = max(max_zero, zero_cnt)
    

input = sys.stdin.readline
n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
max_zero = 0

zeros = [] # 값이 0인 좌표들의 리스트
virus_list = [] # 값이 2인 좌표들의 리스트
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeros.append((i, j))
        elif graph[i][j] == 2:
            virus_list.append((i, j))

# 0인 좌표를 순차적으로 순회하며 3개의 벽을 세우기
for i in range(len(zeros)):
    for j in range(i): 
        for k in range(j): 
            x1, y1 = zeros[i]
            x2, y2 = zeros[j]
            x3, y3 = zeros[k]

            init_graph = copy.deepcopy(graph)
            init_graph[x1][y1], init_graph[x2][y2], init_graph[x3][y3] = 1, 1, 1

            bfs(init_graph, n, m, virus_list)
        
print(max_zero)