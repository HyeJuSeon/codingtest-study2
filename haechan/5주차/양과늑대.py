def dfs(cur, sheep, wolf, node, info, tree, s_cnt):
    if info[cur] == 0: sheep += 1
    else: wolf -= 1

    if sheep + wolf > 0: # 양이 더 많은 경우
        if sheep > s_cnt[-1]: # 현재 최대 양의 수보다 많으면 추가
            s_cnt.append(sheep)
        node += tree[cur]
        for i, n in enumerate(node): # 현재 노드인 n을 제외한 갈 수 있는 나머지 노드를 넣어준다
            dfs(n, sheep, wolf, node[:i]+node[i+1:], info, tree, s_cnt)
    else:
        return

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for a, b in edges:
        tree[a].append(b)

    s_cnt = [0]
    dfs(0, 0, 0, [], info, tree, s_cnt)
    return max(s_cnt)