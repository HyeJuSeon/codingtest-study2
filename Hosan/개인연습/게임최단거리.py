from collections import deque

def solution(maps) :

    answer = -1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    endx = len(maps)-1
    endy = len(maps[0])-1 #maps[1]이 없으면 어쩔건데...?
    visited = [[0 for _ in range(endy + 1)] for _ in range(endx + 1)]
    deq = deque()
    deq.append([0,0])
    visited[0][0] = 1
    while deq :
        curx, cury= deq.popleft()
        if curx == endx and cury == endy :
            return visited[curx][cury]
        else :
            for i in range(4) :
                mx = curx + dx[i]
                my = cury + dy[i]
                if 0 <= mx <= endx and 0 <= my <= endy :
                    if maps[mx][my] == 1 and visited[mx][my] == 0 :
                        deq.append([mx,my])
                        visited[mx][my] = visited[curx][cury] + 1
    return answer
