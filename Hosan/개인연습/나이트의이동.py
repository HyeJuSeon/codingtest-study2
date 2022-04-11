import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
movex=[-1,-2,-2,-1,1,2,2,1]
movey=[2,1,-1,-2,-2,-1,1,2]

def BFS(deq, toX, toY, field):
    while deq:
        curX, curY, count = deq.popleft()
        if curX == toX and curY == toY:
            return count
        else:
            for i in range(8):
                dx = curX + movex[i]
                dy = curY + movey[i]
                if size > dx >= 0 and size > dy >= 0:
                    if field[dx][dy] == 0:
                        deq.append([dx, dy, count + 1])
                        field[dx][dy] = 1
for i in range(N) :
    size = int(input())
    fromX, fromY = map(int, input().split())
    toX, toY = map(int, input().split())
    field = [[0] * size for _ in range(size)]
    deq = deque()
    deq.append([fromX, fromY, 0])
    result = -1
    print(BFS(deq, toX, toY, field))




