import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().split(" "))
visited = [[0 for _ in range(row)] for _ in range(col)]
field = []
deq = deque()
day = 1
movex = [1, -1, 0, 0]
movey = [0, 0, 1, -1]

for i in range(col) :
    tmp = list(map(int, input().strip().split(" ")))
    for j in range(len(tmp)) :
        if tmp[j] == 1 :
            deq.append([i, j, 0])
    field.append(tmp)
#입력 완료
while deq :
    curx, cury, curday = deq.popleft()
    if visited[curx][cury] == 0 :
        visited[curx][cury] = curday
        for i in range(4) :
            nx = curx + movex[i]
            ny = cury + movey[i]
            if 0 <= nx < col and 0 <= ny < row and field[nx][ny] == 0:
                deq.append([curx + movex[i], cury + movey[i], curday + 1])
                field[nx][ny] = 1
flag = True
result = 0
for i in range(col) :
    for j in range(row) :
        if field[i][j] == 0 :
            result = -1
            flag = False
            break
        if visited[i][j] > result :
            result = visited[i][j]
    if flag == False :
        break
print(result)
