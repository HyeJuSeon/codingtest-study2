from collections import defaultdict
def solution(N, road, K):
    answer = 0
    print(road)
    cost = [c[2] for c in road]
    road_lst = [sorted(r[:2]) for r in road]
    road_lst.sort()

    graph = defaultdict(list)
    for key,value in road_lst:
        graph[key] += [value]

    print(graph)
    print(cost, road_lst)
    return answer

def dfs(graph, v, visited):

    visited[v] = True
    return

solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)