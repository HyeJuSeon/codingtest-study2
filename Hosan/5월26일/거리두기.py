from collections import deque

dx = [0, 0, 1, -1]
dy=  [1, -1, 0, 0]

def check(field) :
    start = []
    for i in range(5) :
        for j in range(5) :
            if field[i][j] == "P" :
                start.append([i, j, 0])
    if len(start) == 0 :
        return 1
    for i in range(len(start)) :
        deq = deque()
        deq.append(start[i])
        visited = [[0 for _ in range(5)]for _ in range(5)]
        visited[start[i][0]][start[i][1]] = 1
        while deq :
            tj, tk, distance = deq.popleft()
            for i in range(4) :
                mx = tj + dx[i]
                my = tk + dy[i]
                if mx >= 0 and mx < 5 and my >= 0 and my < 5 and visited[mx][my] == 0:
                        if field[mx][my] == "P" and distance <= 2 :
                            return 0
                        if field[mx][my] == "O" :
                            if distance + 1 < 2 :
                                deq.append([mx, my, distance + 1])
                                visited[mx][my] = 1
    return 1

def solution(places): # 5 places matrix 5x5
    answer = []
    for i in range(len(places)) :
        answer.append(check(places[i]))
    return answer

field = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(field))