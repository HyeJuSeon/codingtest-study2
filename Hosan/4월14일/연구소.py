import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

col, row = map(int, input().split())
field = []
zeros = []
virus = []
movex = [1, -1, 0 ,0]
movey = [0, 0, 1, -1]
result = 0

def dfs(field2, virus) :
    dq = deque()
    for i in virus :
        dq.append(i)
    while dq :
        x, y = dq.popleft()
        for i in range(4) :
            dx = x + movex[i]
            dy = y + movey[i]
            if len(field2) > dx >= 0 and len(field2[1]) > dy >= 0 :
                if field2[dx][dy] == 0 :
                    field2[dx][dy] = 2
                    dq.append((dx, dy))
    global result
    cnt = 0
    for i in range(col):
        cnt += field2[i].count(0)
    result = max(result, cnt)

for i in range(col) :
    tmp = list(map(int, input().split()))
    for j in range(row) :
        if tmp[j] == 0 :
            zeros.append((i,j))
        if tmp[j] == 2 :
            virus.append((i,j))
    field.append(tmp)

for perm in combinations(zeros, 3) :
    field[perm[0][0]][perm[0][1]] = 1
    field[perm[1][0]][perm[1][1]] = 1
    field[perm[2][0]][perm[2][1]] = 1
    tmp_field = copy.deepcopy(field)
    dfs(tmp_field, virus)
    field[perm[0][0]][perm[0][1]] = 0
    field[perm[1][0]][perm[1][1]] = 0
    field[perm[2][0]][perm[2][1]] = 0
print(result)







