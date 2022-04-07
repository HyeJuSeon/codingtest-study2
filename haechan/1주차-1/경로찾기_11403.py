'''백준 11403 - 경로찾기'''

from collections import deque

def bfs(n, node, graph):
    visited = [0] * n
    dq = deque()
    dq.append(node)

    while dq:
        node = dq.popleft()

        # 그래프의 모든 정점을 다 순회(다른 노드를 통해 다시 자기자신으로 돌아오는 경로까지)
        for i, target_node in enumerate(graph[node]):
            if visited[i] == 0 and target_node == 1:
                visited[i] = 1
                dq.append(i)

    return visited

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for node in range(n):
    result = bfs(n, node, graph)
    print(" ".join(map(str, result)))