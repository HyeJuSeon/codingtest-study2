from collections import deque
def find_p(place):
    p_lst = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                p_lst.append((i, j))
    return p_lst

def solution(places):
    answer = []
    n = len(places)
    for p in places:
        queue = deque(find_p(p))
        # 응시자가 없거나 한 명밖에 없으면 바로 1 추가
        if len(queue) < 2:
            answer.append(1)
            continue
        flag = 0
        while queue:
            y, x = queue.popleft()
            # pop한 응시자를 제외한 나머지 응시자가 없을 때
            if not queue:
                answer.append(1)
                break
                
            for k in queue:
                y_dist, x_dist = k[0]-y, k[1]-x
                dist = abs(y_dist) + abs(x_dist)
                # 응시자 사이 거리가 1일 때는 무조건 지키지 않은 경우
                if dist == 1:
                    flag = 1
                    break
                elif dist == 2:
                    # 대각선 파티션 여부 확인
                    # "PX..."
                    # "XP..."
                    if y_dist and x_dist:
                        if p[y+y_dist][x] != "X" or p[y][x+x_dist] != "X":
                            flag = 1
                            break
                    # 세로 사이의 파티션 여부 확인 
                    # "P..."
                    # "X..."
                    # "P..."
                    elif y_dist: 
                        if p[y+1][x] != "X":
                            flag = 1
                            break
                    # 가로 사이의 파티션 여부 확인
                    # "PXP"
                    elif x_dist:
                        if p[y][x+1] != "X":
                            flag = 1
                            break
            if flag:
                answer.append(0)
                break 
        
    return answer