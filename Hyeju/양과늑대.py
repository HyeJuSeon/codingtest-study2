from collections import defaultdict

def solution(info, edges):
    g = defaultdict(list)
    for p, c in edges:
        g[p].append(c)

    def dfs(curr, s_cnt, w_cnt, path):
        if info[curr]:
            w_cnt += 1
        else:
            s_cnt += 1
        if s_cnt <= w_cnt:
            return 0
        ans = s_cnt
        for p in path:
            for next in g[p]:
                if next not in path:
                    path.append(next)
                    ans = max(ans, dfs(next, s_cnt, w_cnt, path))
                    path.pop()
        return ans
    answer = dfs(0, 0, 0, [0])
    return answer

# print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))