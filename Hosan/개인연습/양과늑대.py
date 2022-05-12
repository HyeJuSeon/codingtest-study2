def solution(info, edges) :
    def dfs(sheep, wolf, node, hist):
        if info[node] == 1:
            wolf += 1
        else:
            sheep += 1
        if sheep <= wolf:
            return 0
        Max = sheep
        for i in hist:  # 지금까지 지나온 모든 경로에 대하여
            for j in dic[i]:  # 연결되어있는 모든 노드 탐색
                if j not in hist: #아직 지나온적이 없는 노드가 있다면
                    hist.append(j) #방문할 수 있으므로 (어떻게든 연결되어있으므로) history에 추가
                    Max = max(Max, dfs(sheep, wolf, j, hist))
                    hist.pop() #전부 방문 후에는 다음 i를 위해 pop
        return Max
    dic = {}
    for i in edges :
        x, y = i
        if x not in dic.keys() :
            dic[x] = [y]
        else :
            dic[x].append(y)
        if y not in dic.keys() :
            dic[y] = [x]
        else :
            dic[y].append(x)
    return dfs(0,0,0,[0])