from itertools import combinations
import math

n=int(input())
ability=[list(map(int, input().split())) for _ in range(n)]
arr=[i for i in range(n)]
min_value=math.inf

for combi in combinations(arr,n//2):
    start,link=0,0
    # arr에서 구한 팀 조합(combi)를 뺀 나머지 조합을 저장한 li
    li=list(set(arr)-set(combi))

    # 각 팀의 조합에서 2명씩 조합을 또 구해서 능력치를 더해줌
    for c in combinations(combi,2):
        start+=(ability[c[0]][c[1]]+ability[c[1]][c[0]])
    
    for c in combinations(li,2):
        link+=(ability[c[0]][c[1]]+ability[c[1]][c[0]])
    
    # 해당 조합에서 능력치 차이가 현재 최소 값보다 작으면 그 값을 최소값으로 저장
    min_value=min(abs(start-link),min_value)

print(min_value)