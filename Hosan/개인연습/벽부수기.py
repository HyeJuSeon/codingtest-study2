import sys
from collections import deque
input = sys.stdin.readline
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, input().split())
field = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
#입력받기 완료
visited[0][0][0] = 1
deq = deque()
deq.append((0, 0, 0, 1))
flag = False
def bfs() :
    while deq :
        curX, curY, crushed, count = deq.popleft()
        if curX == N-1 and curY == M-1 :
            return count
        for i in range(4) :
                dx = curX + dir[i][0]
                dy = curY + dir[i][1]
                if N > dx >= 0 and M > dy >= 0 and  visited[dx][dy][crushed] == 0:
                        if field[dx][dy] == 0 :
                            deq.append((dx,dy,crushed, count + 1))
                            visited[dx][dy][crushed] = 1
                        if crushed == 0 and field[dx][dy] == 1:
                            deq.append((dx,dy,1, count + 1))
                            visited[dx][dy][1] = 1
    return -1

print(bfs())
