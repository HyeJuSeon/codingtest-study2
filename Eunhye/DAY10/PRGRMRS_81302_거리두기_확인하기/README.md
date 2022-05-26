## 풀이

find_p 함수를 만들어주어 각 대기실의 응시자의 위치를 찾아 주었습니다.

응시자가 없거나 한 명밖에 없으면 거리두기를 준수하고 있기 때문에 바로 1을 추가해주었고, queue를 pop해주며 각각의 응시자들이 나머지 응시자들과 거리두기를 지키고 있는지 체크해주었습니다.

한 명이라도 준수하고 있지 않다면 더 돌아줄 필요없이 바로 break해주어 0을 추가해주었습니다.

## 코드

```python
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
```
