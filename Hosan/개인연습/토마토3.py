import sys
from collections import deque

input = sys.stdin.readline
mx = [-1,1,0,0,0,0]
my = [0,0,-1,1,0,0]
mh = [0,0,0,0,-1,1]
m,n,h = map(int, input().split())
field = [[[-1 for _ in range(m)]for _ in range(n)]for _ in range(h)]
deq = deque()
for i in range(h) :
    for j in range(n) :
        tmp = list(map(int, input().split()))
        for z in range(m) :
            num = tmp[z]
            field[i][j][z] = num
            if num == 1 :
                field[i][j][z] = 0
                deq.append((i, j, z))
            if num == 0:
                field[i][j][z] = -3
def BFS() :
    while deq:
        curh, curx, cury = deq.popleft()
        for i in range(6):
            dh = curh + mh[i]
            dx = curx + mx[i]
            dy = cury + my[i]
            if h > dh >= 0 and n > dx >= 0 and m > dy >= 0:
                if field[dh][dx][dy] == -3:
                    deq.append((dh, dx, dy))
                    field[dh][dx][dy] = field[curh][curx][cury] + 1
    Max = 0
    for i in range(h):
        for j in range(n):
            for z in range(m):
                if field[i][j][z] == -3:
                    return -1
                else:
                    if field[i][j][z] > Max:
                        Max = field[i][j][z]
    return Max
print(BFS())

