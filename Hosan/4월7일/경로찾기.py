import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
length = int(input())
field = {}

def dfs(i, j , field, visited) :
    visited[i][j] = 1
    if j in field[i] :
        return 1
    else :
        for items in field[i] :
            if visited[items][j] != 1 :
                result = dfs(items, j, field, visited)
                if result == 1 :
                    return 1
    return 0


for i in range(length) :
    tmp = list(map(int, input().split(" ")))
    field[i] = []
    for j in range(length) :
        if tmp[j] == 1 :
            field[i].append(j)

for i in range(length) :
    for j in range(length) :
        visited = [[0 for _ in range(length)] for _ in range(length)]
        print(str(dfs(i, j, field, visited)), end=' ')
    print("")
