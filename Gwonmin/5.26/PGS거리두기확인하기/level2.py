# 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# |r1 - r2| + |c1 - c2| < 3
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다
# 테이블, 파티션, 응시자
from collections import deque
#bfs

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(places):
    answer = []

    for p in places:
        graph = [[o for o in s] for s in p]

        def bfs(x, y):
            visit = [[0] * 5 for _ in range(5)]
            dq = deque()
            ori_x = x
            ori_y = y
            dq.append((x,y))

            while dq:
                x,y = dq[0]
                visit[x][y] = 1
                dq.popleft()
                # print(*visit,sep='\n')
                # print('------------')
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == 0 and graph[nx][ny] != "X":
                        visit[nx][ny] = 1
                        dq.append((nx,ny))
                        if graph[nx][ny] == "P":
                            if abs(ori_x-nx)+abs(ori_y-ny) < 3:
                                return 0

                        elif abs(ori_x-nx)+abs(ori_y-ny) > 2:
                            return 1

            return 1

        temp = 1
        for y in range(5):
            for x in range(5):
                if graph[x][y] == 'P':
                    if bfs(x,y) != 1:
                        temp = 0

        answer.append(temp)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
