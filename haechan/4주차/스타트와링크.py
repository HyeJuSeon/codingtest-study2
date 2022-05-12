'''백준 - 스타트와 링크'''

from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
person = [i for i in range(n)]

result_min = 10000
for A_team in combinations(person, n//2): # 전체 인원의 절반으로 팀 조합 구성
    A_abil, B_abil = 0, 0
    B_team = set(person) - set(A_team)
    for i, j in combinations(A_team, 2): # 같은 팀 중 2명씩 조합 만들기
        A_abil += graph[i][j]
        A_abil += graph[j][i]

    for i, j in combinations(B_team, 2):
        B_abil += graph[i][j]
        B_abil += graph[j][i]

    result_min = min(result_min, abs(A_abil-B_abil)) # 차이가 최소인 값 저장

print(result_min)