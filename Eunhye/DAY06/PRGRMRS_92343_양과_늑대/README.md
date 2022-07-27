## 풀이

DFS로 풀어주었습니다.  

visited로 방문한 노드를 체크해주며 돌아줍니다. is_wolf를 체크하며 해당 노드에 양이나 늑대가 있는지 확인해주었습니다. 양이라면 sheep를, 늑대라면 wolf의 숫자를 늘려주며, 늑대의 숫자가 양의 숫자와 같거나 크다면 혹은 더 이상 나아갈수 없는 leaf 노드라면 return 해주어 재귀호출을 종료해줍니다.  

모든 경우의 수를 체크해주며 모을 수 있는 양의 최대 마리 수를 구해줍니다.
 

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
