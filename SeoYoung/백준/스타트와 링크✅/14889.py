from itertools import combinations
import math

n=int(input())
ability=[list(map(int, input().split())) for _ in range(n)]
arr=[i for i in range(n)]
min_value=math.inf

for combi in combinations(arr,n//2):
    start,link=0,0
    li=list(set(arr)-set(combi))

    for c in combinations(combi,2):
        start+=(ability[c[0]][c[1]]+ability[c[1]][c[0]])
    
    for c in combinations(li,2):
        link+=(ability[c[0]][c[1]]+ability[c[1]][c[0]])
    
    min_value=min(abs(start-link),min_value)

print(min_value)