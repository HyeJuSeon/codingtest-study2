import sys
input = sys.stdin.readline

col, row = map(int, input().split(" "))
field = [[0 for _ in range(row)] for _ in range(col)]
visited = [[0 for _ in range(row)] for _ in range(col)]
moveX = [1, -1, 0, 0] #오른쪽 아래쪽 왼쪽 위쪽
moveY = [0, 0, 1, 1]
Min = 1000000
for i in range(col) :
    line = input()
    for j in range(row) :
        field[i][j] = int(line[j])

def DFS(field, x, y, count) :
    visited[x][y] = 1
    if x == col - 1 and y == row - 1 :
        global Min
        if Min > count :
            Min = count
    else :
        for k in range(4) :
            mx = x + moveX[k]
            my = y + moveY[k]
            if mx >= 0 and mx < col and my >= 0 and my < row :
                if visited[mx][my] == 0 and field[mx][my] == 1:
                    DFS(field, mx, my, count + 1)
                    visited[mx][my] = 0 #다음 탐색에서도 방문 가능해야하므로 0으로 다시 초기화
        return Min
print(DFS(field, 0, 0, 1))

