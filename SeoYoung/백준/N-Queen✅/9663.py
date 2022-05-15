N=int(input())
row=[0]*N
result=0

def canPlace(depth):
    for i in range(depth):
        # 같은 열에 위치하거나 대각선에 위치하면 false
        if row[depth]==row[i] or abs(row[depth]-row[i])==depth-i:
            return False
    return True

def dfs(depth):
    global result
    if depth==N:
        result+=1
        return 
    else:
        for i in range(N):
            row[depth]=i
            if canPlace(depth):
                dfs(depth+1)

dfs(0)
print(result)