import sys
input = sys.stdin.readline

n=int(input())
house=[list(map(int, input().split())) for _ in range(n)]
count=0
dfs(0,1,0)

print(count)

# dir = 0(가로) dir=1(세로) dir=2(대각선)
def dfs(x,y,dir):
    global count
    if x==n-1 and y==n-1:
        count+=1
        return 
    
    # 방향에 관계없이 대각선 방향은 모두 갈 수 있으므로 대각선 방향 모두 탐색
    # 대각선 방향은 가로 세로 대각선 방향 모두 0이어야 탐색가능
    if x+1<n and y+1<n:
        if house[x+1][y+1]==0 and house[x+1][y]==0 and house[x][y+1]==0:
            dfs(x+1,y+1,2)
    
    # 가로방향이나 대각선 방향일 때 가로방향 탐색
    if dir==0 or dir==2:
        if y+1<n and house[x][y+1]==0:
            dfs(x,y+1,0)
    
    # 세로방향이나 대각선 방향일 때 세로 방향 탐색
    if dir==1 or dir==2:
        if x+1<n and house[x+1][y]==0:
            dfs(x+1,y,1)


