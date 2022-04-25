## 풀이

## 코드

```from itertools import combinations
#조합을 활용한 완전탐색

n = int(input())

ij_lst = [list(map(int,input().split())) for _ in range(n)]
member = int(n/2)

start_team = list(combinations([i for i in range(n)],member))
link_team = []

for t in start_team:
    lst = []
    for i in range(n):
        if i not in t:
            lst.append(i)
    link_team.append(lst)

min_dif = 999999999999

def team_point(ij_lst,case):
    return ij_lst[case[0]][case[1]] + ij_lst[case[1]][case[0]]

for s, l in zip(start_team, link_team):
    point_s = 0
    point_l = 0
    for c in list(combinations(s,2)):
        point_s += team_point(ij_lst,c)
    for c in list(combinations(l,2)):
        point_l += team_point(ij_lst,c)
    min_dif = min(min_dif, abs(point_s-point_l))

print(min_dif)
```
