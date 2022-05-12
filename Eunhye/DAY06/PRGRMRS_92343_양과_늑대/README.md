## 풀이

## 코드

```python
def dfs(node, sheep, wolf, nodes, visited):
    global result, is_wolf, adj
    n_nodes = list(set(nodes + adj[node]))
    if sheep <= wolf or not n_nodes:
        return
    for new_node in n_nodes:
        if not visited[new_node]:
            visited[new_node] = 1
            if is_wolf[new_node] == 0:
                dfs(new_node, sheep+1, wolf, n_nodes, visited)
            else:
                dfs(new_node, sheep, wolf+1, n_nodes, visited)
            visited[new_node] = 0
    result = max(result, sheep)

def solution(info, edges):
    global result, is_wolf, adj
    is_wolf = info
    result = 1
    adj = [[] for _ in range(len(info))]
    visited = [0 for _ in range(len(info))]
    for i, j in edges:
        adj[i].append(j)
    visited[0] = 1
    dfs(0, 1, 0, [0], visited)
    return result
```
